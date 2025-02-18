# Nested if Statements
sport = input("Enter the Sport: ").lower()
p1_score = int(input("Score of Player 1: "))
p2_score = int(input("Score of Player 2: "))

if sport == "football":
    if p1_score > p2_score:
        print("Player 1 wins!")
    elif p1_score < p2_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

elif sport == "basketball":
    if p1_score > p2_score:
        print("Player 1 wins!")
    elif p1_score < p2_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")

else:
    print("Invalid sport!")
    