#!/bin/bash

trap "break" INT # Trap the INT (interrupt) signal

while true; do
	mpg123 -@ ~/music/playlist.txt -q -v
done
