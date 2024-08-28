import random


Easy_Lvl_Attempts= 10
Hard_Lvl_Attempts= 5

def difficulty_lvl(chosen_level):
    if chosen_level == "easy":
        print("You'll get total 10 attempts to guess the numbers. ")
        return Easy_Lvl_Attempts
    elif chosen_level == "hard":
        print("You'll get total 5 attempts to guess the numbers. ")
        return Hard_Lvl_Attempts
    else:
        print("You have choosen a wrong level so play again.")
        return

def check_answer(number_guess, answer, attemtps):
    if number_guess<answer:
        print("Your guess is too low")
        return attemtps-1
    elif number_guess>answer:
        print("Your answer is too high")
        return attemtps-1
    else:
        print(f"Your guess is correct... The answer is {answer}")
        

def game():
    

    print("Let me think of a number between 1 to 100")
    answer = random.randint(1,100)

    level = input("Choose level of difficulty.... Type 'easy' or 'hard':  " )
    attempts = difficulty_lvl(level)
    if attempts is None:
        print("You have entered wrong difficulty level... Play again. ")
        return
    guessed_number = 0
    while guessed_number!=answer and attempts>0:
        print(f"You have {attempts} attempts remaining to guess the number. ")
        guessed_number = int(input("Guess a number: "))
        attempts = check_answer(guessed_number, answer, attempts)

        if attempts==0:
            print("You are out of guesses.. You loose.")
            return
        elif guessed_number!=answer:
            print("Wrong guess... Guess again")
        else:
            print("You are correct.. You won.")


game()

        
