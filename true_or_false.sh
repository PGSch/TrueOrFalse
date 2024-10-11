#!/usr/bin/env bash

SCORE=0
CORRECT_ANSWERS=0
SCORE_FILE="scores.json"

# Print the welcoming message
echo "Welcome to the True or False Game!"
curl --silent --output ID_card.txt http://127.0.0.1:8000/file.txt
echo -n "Enter username: "
read -r username
echo -n "Enter password: "
read -r -s password
echo ""

LOGIN_RESPONSE=$(curl --silent --write-out "HTTPSTATUS:%{http_code}" \
    --cookie-jar cookie.txt \
    --user "$username":"$password"\
    http://127.0.0.1:8000/login)

HTTP_STATUS=$(echo "$LOGIN_RESPONSE" | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')

# Remove status code from body
LOGIN_BODY=$(echo "$LOGIN_RESPONSE" | sed -e 's/HTTPSTATUS\:.*//g')

# Terminate if wrong credentials (e.g., status code is not 200)
if [[ $HTTP_STATUS -ne 200 ]]; then
    echo "Login failed: $LOGIN_BODY"
    exit 1
fi

echo "Login successful! Starting game..."


# Function to display the menu
menu() {
    echo ""
    echo "0. Exit"
    echo "1. Play a game"
    echo "2. Display scores"
    echo "3. Reset scores"
    echo -n "Enter an option: "
    read -r option
}

# Function to play the game
play_game() {
    # Reset scores at the beginning of each game
    SCORE=0
    CORRECT_ANSWERS=0

    # Set seed for RANDOM for consistent results
    RANDOM=4096

    echo -n "What is your name?"
    read PLAYER_NAME

    # Array of positive responses
    responses=("Perfect!" "Awesome!" "You are a genius!" "Wow!" "Wonderful!")

    # Start the game loop
    while true; do
        # Connect to the /game endpoint  to get a question and answer
        GAME_RESPONSE=$(curl --silent --cookie cookie.txt http://127.0.0.1:8000/game)

        # Parse the question and answer from the JSON response
        QUESTION=$(echo "$GAME_RESPONSE" | sed 's/.*"question": *"\{0,1\}\([^,"]*\)"\{0,1\}.*/\1/')
        ANSWER=$(echo "$GAME_RESPONSE" | sed 's/.*"answer": *"\{0,1\}\([^,"]*\)"\{0,1\}.*/\1/')
        
        # Print question and read response
        echo "$QUESTION"
        echo -n "True or False? "
        read USER_RESPONSE

        # Compare response to actual answer
        if [[ "$USER_RESPONSE" == "$ANSWER" ]]; then
            # Correct reponse
            let SCORE+=10
            let CORRECT_ANSWERS+=1

            ## Select random positive response
            idx=$((RANDOM % 5))
            echo "${responses[$idx]}"
        else
            # Wrong response
            echo "Wrong answer, sorry!"
            echo "$PLAYER_NAME you have $CORRECT_ANSWERS correct answer(s)."
            echo "Your score is $SCORE points."

            save_score "$PLAYER_NAME" "$SCORE"
            break
        fi
    done
}

# Function to save scores to scores.json
save_score() {
    local PLAYER_NAME=$1
    local PLAYER_SCORE=$2
    local DATE=$(date +%Y-%m-%d)

    # Check if scores.json exists
    if [ ! -f "$SCORE_FILE" ]; then
        # Initialize json array for later apped via 'jq'
        echo "[]" > "$SCORE_FILE"
    fi

    # Append new score
    jq ". + [{\"User\": \"$PLAYER_NAME\", \"Score\": \"$PLAYER_SCORE\", \"Date\": \"$DATE\"}]" "$SCORE_FILE" \
        > tmp.json && mv tmp.json "$SCORE_FILE"
}
 
# Function to display scores from score.json
display_scores() {
    if [ -f "$SCORE_FILE" ] && [ -s "$SCORE_FILE" ]; then
        echo "Player scores"
        # jq to format JSON and display nicely
        jq -r '.[] | "User: \(.User), Score: \(.Score), Date: \(.Date)"' "$SCORE_FILE"
    else
        echo "File not found or no scores in  it!"
    fi
}

# Function to reset scores (delete scores.json)
reset_scores() {
    if [ -f "$SCORE_FILE" ]; then
        rm "$SCORE_FILE"
        echo "File deleted successfully! Scores reset!"
    else
        echo "File not found or no scores in it!"
    fi
}

# Define the main menu loop
while true; do
    # Display the menu options
    menu

    # Handle the different options
    case $option in
        0)
            echo "See you later!"
            exit 0  # Exit the program
            ;;
        1)
            #echo "Playing game"
            play_game
            ;;
        2)
            #echo "Displaying scores"
            display_scores
            ;;
        3)
            #echo "Resetting scores"
            reset_scores
            ;;
        *)
            echo "Invalid option!"
            ;;
    esac
done

