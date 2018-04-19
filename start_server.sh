#!/bin/sh

# This script runs ngrok and starts the python server in the background
# just one file to start things off

./ngrok http 3000 &
python3 main.py
