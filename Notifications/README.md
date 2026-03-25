# GLaDOS - Claude Code Sound Hooks + Telegram Notifications

## What This Does

Plays GLaDOS-themed audio cues during Claude Code sessions and sends Portal-themed Telegram notifications for long tasks:

| Event | Sound File | Trigger | Telegram |
|---|---|---|---|
| Session start | `Hello-2.aiff` | Claude Code launches | No |
| Session end | `Bye-2.aiff` | Claude Code exits | No |
| Task start | `Start-2.aiff` | User sends a prompt AND Claude is still working 10 seconds later | No |
| Task finish | `Finish-2.aiff` | Claude finishes a response AND the task took >= 1 minute | Yes |

The Start/Finish sounds have timing thresholds to avoid playing on quick exchanges. Telegram notifications are sent only for long tasks (>= 1 minute) and include the last assistant message from the session transcript.

## Setup Instructions

### Step 1: Copy audio files and scripts

Create the hooks directory and copy everything:

```bash
mkdir -p ~/.claude/hooks/sounds
cp -r sounds/GLaDOS sounds/JARVIS ~/.claude/hooks/sounds/
cp on-prompt.sh on-stop.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/on-prompt.sh ~/.claude/hooks/on-stop.sh
```

### Step 2: Update paths inside the shell scripts

The scripts reference `~/.claude/hooks/sounds/GLaDOS/` for the audio files. If you placed the files in a different directory, edit both scripts to update the `afplay` paths.

To use JARVIS sounds instead, change `GLaDOS` to `JARVIS` and remove the `-2` suffix from filenames in the scripts and `settings.json`.

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

6. Edit `~/.claude/hooks/on-stop.sh` and replace the placeholder on line 6:
   ```bash
   TELEGRAM_BOT_TOKEN="PASTE_BOT_TOKEN_HERE"   # ← replace with your bot token
   ```
   The chat ID on line 7 also needs to be replaced with your own.

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

**If `"hooks"` already exists** in `settings.json`, append the 4 hook arrays (`SessionStart`, `SessionEnd`, `UserPromptSubmit`, `Stop`) into the existing `"hooks"` object. Do not overwrite other hook event types that may already be configured.

### Step 5: Verify

Restart Claude Code. You should hear `Hello-2.aiff` on launch. To test Telegram, run a task that takes over 1 minute — you should receive a Portal-themed notification on Telegram when it finishes.

## File Inventory

| File | Purpose |
|---|---|
| `sounds/GLaDOS/Hello-2.aiff` | Played on session start |
| `sounds/GLaDOS/Bye-2.aiff` | Played on session end |
| `sounds/GLaDOS/Start-2.aiff` | Played when a task exceeds 10 seconds |
| `sounds/GLaDOS/Finish-2.aiff` | Played when a task exceeds 1 minute |
| `sounds/JARVIS/` | Alternative JARVIS voice pack |
| `on-prompt.sh` | Script that saves a timestamp and schedules Start sound after 10s delay |
| `on-stop.sh` | Script that checks elapsed time, plays Finish sound, extracts last assistant message, and sends Portal-themed Telegram notification if >= 1 minute |
| `hooks.json` | The hooks configuration to merge into `~/.claude/settings.json` |
| `README.md` | This file |

## How the Timing Mechanism Works

- `on-prompt.sh` (runs on every user prompt):
  1. Writes current Unix timestamp to `/tmp/claude-sound-ts`
  2. Spawns a background process that sleeps 10 seconds, then checks if the timestamp file still exists and matches — if so, plays `Start-2.aiff`

- `on-stop.sh` (runs when Claude finishes responding):
  1. Reads the timestamp from `/tmp/claude-sound-ts`
  2. Reads the session ID from stdin to locate the session transcript
  3. Calculates elapsed time since the prompt
  4. Deletes `/tmp/claude-sound-ts` (this also cancels any pending Start sound that hasn't played yet)
  5. If elapsed >= 60 seconds: plays `Finish-2.aiff`, extracts the last assistant text message from the session JSONL, and sends a Portal-themed Telegram notification with the message content, duration, and completion time

This means:
- Quick exchanges (< 10s): no sounds, no notification
- Medium tasks (10s - 1min): only Start plays, no notification
- Long tasks (>= 1min): Start plays, then Finish plays + Telegram notification

## Telegram Notification Format

Notifications use a Portal theme:
```
This was a triumph!
I'm making a note here:
HUGE SUCCESS!

[Last assistant message from the session]

The task took Xm Ys and was finished at HH:MM.
```

## Platform Requirements

- **macOS**: Works out of the box (`afplay` and `curl` are built-in)
- **Linux**: Replace `afplay` with `paplay` (PulseAudio), `aplay` (ALSA), or `mpv --no-video` in all 4 locations (2 in `settings.json`, 1 in each `.sh` script). Convert `.aiff` files to `.wav` or `.ogg` if the chosen player doesn't support AIFF. `curl` is typically available.
- **Windows (WSL)**: Use `powershell.exe -c "(New-Object Media.SoundPlayer 'path/to/file.wav').PlaySync()"` or install `sox` (`play` command). Audio files may need conversion to `.wav`. `curl` is available in WSL.
