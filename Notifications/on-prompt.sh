#!/bin/bash
# Save timestamp and schedule Start sound after 15s delay.
# If Stop fires before 15s, the timestamp file will be removed,
# cancelling the scheduled sound.
TS=$(date +%s)
echo "$TS" > /tmp/claude-sound-ts
(sleep 15 && [ -f /tmp/claude-sound-ts ] && [ "$(cat /tmp/claude-sound-ts)" = "$TS" ] && afplay ~/.claude/sounds/Start.aiff) &
