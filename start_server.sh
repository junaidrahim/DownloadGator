#!/bin/sh

# This script runs ngrok and starts the python server in the background
# just one file to start things off

# make sure you have ngrok authtoken configured so that your hosting runs doesnt run for a limited time
# Instructions are in the README

./ngrok http 3000 &
python3 main.py
