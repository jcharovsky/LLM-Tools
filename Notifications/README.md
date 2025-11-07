# JARVIS - Claude Code Sound Hooks + Telegram Notifications

## What This Does

Plays audio cues during Claude Code sessions and sends Telegram notifications for long tasks:

| Event | Sound File | Trigger | Telegram |
|---|---|---|---|
| Session start | `Hello.aiff` | Claude Code launches | No |
| Session end | `Bye.aiff` | Claude Code exits | No |
| Task start | `Start.aiff` | User sends a prompt AND Claude is still working 15 seconds later | No |
| Task finish | `Finish.aiff` | Claude finishes a response AND the task took >= 2 minutes | Yes |

The Start/Finish sounds have timing thresholds to avoid playing on quick exchanges. Telegram notifications are sent only for long tasks (>= 2 minutes).

## Setup Instructions

### Step 1: Copy audio files and scripts

Create the sounds directory and copy all `.aiff` and `.sh` files from this folder:

```bash
mkdir -p ~/.claude/sounds
cp Hello.aiff Bye.aiff Start.aiff Finish.aiff on-prompt.sh on-stop.sh ~/.claude/sounds/
chmod +x ~/.claude/sounds/on-prompt.sh ~/.claude/sounds/on-stop.sh
```

### Step 2: Update paths inside the shell scripts

The scripts reference `~/.claude/sounds/` for the audio files. If you placed the files in a different directory, edit both scripts to update the `afplay` paths.

In `on-prompt.sh`, update the path on the last line:
```
afplay ~/.claude/sounds/Start.aiff
```

In `on-stop.sh`, update the path on line 15:
```
afplay ~/.claude/sounds/Finish.aiff
```

If installing on Linux, replace `afplay` with the appropriate audio player (e.g., `paplay`, `aplay`, or `mpv --no-video`).

### Step 3: Set up Telegram bot

This step enables Telegram notifications for long tasks. If you don't want Telegram notifications, skip this step — the sounds will still work, and the curl command will silently fail with the placeholder values.

1. Open Telegram and message [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow the prompts to create a bot
3. Copy the bot token (looks like `123456:ABC-DEF...`)
4. Send any message to your new bot on Telegram
5. Get your chat ID by running:
   ```bash
   curl -s "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates" | python3 -m json.tool
   ```
   Look for `"chat": { "id": 123456789 }` in the response.

6. Edit `~/.claude/sounds/on-stop.sh` and replace the two placeholders on lines 6-7:
   ```bash
   TELEGRAM_BOT_TOKEN="PASTE_BOT_TOKEN_HERE"   # ← replace with your bot token
   TELEGRAM_CHAT_ID="PASTE_CHAT_ID_HERE"       # ← replace with your chat ID
   ```

7. Test by sending a message manually:
   ```bash
   curl -s -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/sendMessage" \
     -d chat_id="<YOUR_CHAT_ID>" \
     -d text="Test notification from Claude Code."
   ```

### Step 4: Merge hooks into settings.json

The hooks configuration must be added to `~/.claude/settings.json`.

**Target file:** `~/.claude/settings.json` (this is the global Claude Code settings file, NOT project-specific).

**If the file does not exist**, copy `hooks.json` as-is:
```bash
cp hooks.json ~/.claude/settings.json
```

**If the file already exists**, merge the `"hooks"` key from `hooks.json` into the existing JSON object. The `"hooks"` key is a top-level key in `settings.json` alongside other settings like `"alwaysThinkingEnabled"`, `"permissions"`, etc.

Example — if the existing `settings.json` is:
```json
{
  "alwaysThinkingEnabled": true
}
```

After merging it should be:
```json
{
  "hooks": {
    "SessionStart": [ ... ],
    "SessionEnd": [ ... ],
    "UserPromptSubmit": [ ... ],
    "Stop": [ ... ]
  },
  "alwaysThinkingEnabled": true
}
```

**If `"hooks"` already exists** in `settings.json`, append the 4 hook arrays (`SessionStart`, `SessionEnd`, `UserPromptSubmit`, `Stop`) into the existing `"hooks"` object. Do not overwrite other hook event types that may already be configured.

### Step 5: Update paths in hooks.json (if non-default location)

All paths in `hooks.json` assume files are at `~/.claude/sounds/`. If you used a different directory, update these 4 command strings:

1. `"command": "afplay ~/.claude/sounds/Hello.aiff"` — SessionStart
2. `"command": "afplay ~/.claude/sounds/Bye.aiff"` — SessionEnd
3. `"command": "~/.claude/sounds/on-prompt.sh"` — UserPromptSubmit
4. `"command": "~/.claude/sounds/on-stop.sh"` — Stop

### Step 6: Verify

Restart Claude Code. You should hear `Hello.aiff` on launch. To test Telegram, run a task that takes over 2 minutes — you should receive a notification on Telegram when it finishes.

## File Inventory

| File | Purpose |
|---|---|
| `Hello.aiff` | Played on session start |
| `Bye.aiff` | Played on session end |
| `Start.aiff` | Played when a task exceeds 15 seconds |
| `Finish.aiff` | Played when a task exceeds 2 minutes |
| `on-prompt.sh` | Script that saves a timestamp and schedules Start sound after 15s delay |
| `on-stop.sh` | Script that checks elapsed time, plays Finish sound, and sends Telegram notification if >= 2 minutes |
| `hooks.json` | The hooks configuration to merge into `~/.claude/settings.json` |
| `README.md` | This file |

## How the Timing Mechanism Works

- `on-prompt.sh` (runs on every user prompt):
  1. Writes current Unix timestamp to `/tmp/claude-sound-ts`
  2. Spawns a background process that sleeps 15 seconds, then checks if the timestamp file still exists and matches — if so, plays `Start.aiff`

- `on-stop.sh` (runs when Claude finishes responding):
  1. Reads the timestamp from `/tmp/claude-sound-ts`
  2. Calculates elapsed time since the prompt
  3. Deletes `/tmp/claude-sound-ts` (this also cancels any pending Start sound that hasn't played yet)
  4. If elapsed >= 120 seconds: plays `Finish.aiff` AND sends a Telegram notification with duration and completion time

This means:
- Quick exchanges (< 15s): no sounds, no notification
- Medium tasks (15s - 2min): only Start plays, no notification
- Long tasks (>= 2min): Start plays, then Finish plays + Telegram notification

## Telegram Custom Ringtone

A `Finish.mp3` file is included alongside `Finish.aiff`. This is the same audio in MP3 format, which is required by Telegram for uploading custom notification ringtones. To use it, open Telegram notification settings and upload `Finish.mp3` as a custom tone for the bot's chat. This way, Telegram notifications from long tasks will play the same Finish sound on your phone.

## Platform Requirements

- **macOS**: Works out of the box (`afplay` and `curl` are built-in)
- **Linux**: Replace `afplay` with `paplay` (PulseAudio), `aplay` (ALSA), or `mpv --no-video` in all 4 locations (2 in hooks.json, 1 in each .sh script). Convert `.aiff` files to `.wav` or `.ogg` if the chosen player doesn't support AIFF. `curl` is typically available.
- **Windows (WSL)**: Use `powershell.exe -c "(New-Object Media.SoundPlayer 'path/to/file.wav').PlaySync()"` or install `sox` (`play` command). Audio files may need conversion to `.wav`. `curl` is available in WSL.
