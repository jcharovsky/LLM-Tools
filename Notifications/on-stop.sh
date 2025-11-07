#!/bin/bash
# Play Finish sound only if the task took >= 2 minutes.
# Also removes the timestamp file to cancel any pending Start sound.
# Sends a Telegram notification for long tasks.

TELEGRAM_BOT_TOKEN="PASTE_BOT_TOKEN_HERE"
TELEGRAM_CHAT_ID="PASTE_CHAT_ID_HERE"

TS=$(cat /tmp/claude-sound-ts 2>/dev/null || echo 0)
NOW=$(date +%s)
ELAPSED=$((NOW - TS))
rm -f /tmp/claude-sound-ts

if [ "$ELAPSED" -ge 120 ]; then
  afplay ~/.claude/sounds/Finish.aiff
  MINS=$((ELAPSED / 60))
  SECS=$((ELAPSED % 60))
  TIME=$(date +%H:%M)
  curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    -d chat_id="${TELEGRAM_CHAT_ID}" \
    -d text="The render is complete. It took ${MINS}m ${SECS}s and was finished at ${TIME}." \
    > /dev/null 2>&1
fi
