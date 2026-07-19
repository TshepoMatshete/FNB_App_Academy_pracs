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