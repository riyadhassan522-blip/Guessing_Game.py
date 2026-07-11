import random

def play_round(max_lives,max_range):
    print("\n---New Game Started---")
    secret_number = random.randint(1, max_range)
    attempts = 0

    #Adjusts the "warm" hint distance based on how big the range is
    warm_threshold = max(3, max_range // 15)

    print(f"You hae {max_lives} attempts to guess the number between 1 and {max_range}.")

    while attempts < max_lives:
        try:
            guess = int(input(f"[{max_lives - attempts} lives left] Enter your guess: "))

            #Check if the guessnis outside the allowed numbers
            if guess < 1 or guess > max_range:
                print(f"⚠ Out of bounds! Enter a number between 1 and {max_range}.")
                continue # Loops back without costing a life

            attempts += 1

            if guess < secret_number:
                print("Too low!")
                if secret_number - guess<= warm_threshold:
                    print("👉 But you are getting warm!!")
            elif guess > secret_number:
                print("Too high!")
                if guess - secret_number <= warm_threshold:
                    print("👉 But you are getting warm!!")        

            else:
                print(f"🎉 Correct! You won in{attempts} attempts!")
                return True, attempts
        except ValueError:
                print("❌ Invalid input. Please enter a whole number.") # No life ost for typos!

    print(f"💀 Game Over! You ran out of lives. The number was {secret_number}.")
    return False, attempts
def get_difficulty():
    print("\n--- SELECT DIFFICULTY ---")
    print("1. Novice (1-20, 8 lives) | 2. Easy (1-50, 10 lives")
    print("3. Medium (1-100, 7 lives) | 4. Hard (1-200, 5 lives)")
    print("5. Expert (1-500, 3 lives)")

    while True:
        c = input("select difficulty (1-5): ")
        if c == '1': return 8,20
        if c == '2': return 10,50
        if c == '3': return 7,100
        if c == '4': return 5,200   
        if c == '5': return 3,500
        print("Invalid choice. Try again.")

def main():
    print("=====================================")
    print("WELCOME TO THE ULTIMATE GUESSING GAME ")
    print("=====================================")

    games_played = 0
    wins = 0
    losses = 0 
    total_attempts = 0
    best_score = None # Tracks the lowest number of guesses used to win

    while True:
        max_lives, max_range = get_difficulty()
        is_win, round_attempts = play_round(max_lives,max_range)

        games_played += 1
        total_attempts += round_attempts

        if is_win:
            wins += 1
            if best_score is None or round_attempts < best_score:
                best_score = round_attempts
                print("⭐ New Personal Record!⭐")
        else:
            losses += 1
        print("\n============================")
        print("        SCOREBOARD          ")
        print("============================") 
        print(f"🎮 Games Played:     {games_played}")
        print(f"🏆 Wins:             {wins}")
        print(f"💀 Losses:           {losses}")
        print(f"📊 Total Guesses:    {total_attempts}")
        print(f"⭐ Best win          {f'{best_score} guesses' if best_score else 'N/A'}")
        
        replay = input("\nDo you want to play another round? (yes/no): ").lower().strip()
        if replay != 'yes' and replay != 'y':
            print("nThanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()            
         
            

            


