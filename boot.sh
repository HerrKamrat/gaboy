#!/bin/bash
cd "$(dirname "$0")"

find .git/objects/ -size 0 -delete

git pull --ff

./app.py
