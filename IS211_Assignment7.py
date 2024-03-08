import random

random.seed(0)

def roll_dice():
    return random.randint(1, 6)


def player_turn(player_name, current_score):
    turn_total = 0
    while True:
        print(f"{player_name}'s turn:")
        roll = roll_dice()
        print(f"Rolled: {roll}")

        if roll == 1:
            print("Sorry, no points this turn.")
            break
        else:
            turn_total += roll
            print(f"Turn total: {turn_total} Game total: {current_score + turn_total}")

            decision = input("Choose 'r' to roll again or 'h' to hold: ").strip().lower()
            if decision == 'h':
                break

    return turn_total
    

def play_game():
        player_scores = [0, 0]
        player_names = ["Player 1", "Player 2"]

        while all(score < 100 for score in player_scores):
            for i, player_name in enumerate(player_names):
                player_scores[i] += player_turn(player_name, player_scores[i])
                if player_scores[i] >= 100:
                    print(f"{player_name} wins with {player_scores[i]} points!")
                    return
                
if __name__ == "__main__":
    play_game()