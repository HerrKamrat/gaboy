#!/bin/bash

find .git/objects/ -size 0 -delete

git pull --ff

./app.py
