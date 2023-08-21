#!/bin/bash

var="my script"

echo "Hi!" && sleep 2

echo -n "What's your name? " && read user_input
echo -n "Welcome to ${var}, ${user_input}. You're in: " && pwd

echo -n "And your username is "  && whoami
