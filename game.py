import random

# Computer to pick a number 
# Player to guess the number 
# Compare if player guess is higher/lower or matches the computer number
# Tell the player when the guess the correct number and how many guesses it took them
# Extention - Write the code for the computer to guess your number and menu for the player to choose what style of game to play


def player_guess():
    number_range = int(input("Choose the maximum number for the computer to pick a number from: "))
    computer_num = int(random.randint(1,number_range))
    guess_count = 0
    
    while True:
        guess_count +=1
        guess = int(input("Guess a number: "))
        if computer_num == guess:
            print(f"Congradulations you picked the correct number in {guess_count} attempts!")
            break
        elif computer_num < guess:
            print(f"Incorrect guess, the number is smaller than {guess}")
        else:
            print(f"Incorrect guess, the number is greater than {guess}")


def computer_guess():
    low = 1
    high = int(input("What is the highest number in the range for the computer to guess from?: "))
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
       
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


game = " "

while game != "q":
    game = input("Select (p) to pick a number, (g) to guess a number or (q) to quit the game: ").lower()
    if game == "p":
        computer_guess()
    elif game == "g":
        player_guess()
    else:
        print("You did not select a valid option")
