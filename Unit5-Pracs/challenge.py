# The Challenge: “The High-Score Tracker Game”
# Build an interactive program that continuously asks an arcade player for their game
# score.

# 1. Start an intentional infinite loop using while True:.

# 2. Inside the loop, ask the user to enter a game score next to the flashing cursor.

# 3. If they type the word “stop” (clean it up with .strip().lower()), print “Game session ended!” and use a break statement to shut down the loop.

# 4. Otherwise, cast their input into an int, check if the score is greater than 100, and print either “Wow! That’s a new high score!” or “Good try, keep playing!” based on the value.
high_score = 100
while True:
    score_input = input("Enter your game score (or type 'stop' to end): ").strip().lower()
    
    if score_input == "stop":
        print("Game session ended!")
        break
    
    try:
        score = int(score_input)
        if score > high_score:
            print("Wow! That’s a new high score!")
            high_score = score
        else:
            print("Good try, keep playing!")
    except ValueError:
        print("Invalid input. Please enter a valid score or 'stop' to end.")