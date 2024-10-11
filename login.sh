#!/usr/bin/env bash

# Step 1: Print the welcoming message
echo "Welcome to the True or False Game!"

# Step 2: Log in and save the session cookie to cookie.txt
curl --silent \
    --cookie-jar cookie.txt \
    --user admin:123 \
    http://127.0.0.1:8000/login

# Step 3: Connect to the /game endpoint using the saved session cookie
GAME_RESPONSE=$(curl --silent \
    --cookie cookie.txt \
    http://127.0.0.1:8000/game)

# Step 4: Print the response from the /game endpoint
echo "Response: $GAME_RESPONSE"
