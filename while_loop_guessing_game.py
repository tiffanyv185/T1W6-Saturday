# Guessing game

guess_num = 66

user_guess = None

# while user_guess != guess_num:
#     user_guess = int(input("What's your guess?: (between 1 and 10) "))
#     print("incorrect")

# print("correct")

# Make it better by giving hints to users

while user_guess != guess_num:
    user_guess = int(input("guess a number between 1 and 100: "))

    if user_guess < guess_num:
        print("number too low!")
    
    elif user_guess > guess_num:
        print("number too high!")

print("correct!!!!")