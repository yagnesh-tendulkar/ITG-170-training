import random

choices = ["rock","paper","scissors"]

print("Welcome to rock paper scissors game ..")
print("Enter your choice rock , paper or scissors and if you want to quit press Quit")

user_points = 0
bot_points = 0

while True:
    user_input = input("Enter the your choice ::: ").lower().strip()
    if user_input == "quit":
        print(f"The final Score:- User score : {user_points} and Bot Score : {bot_points}")
        print("You ended the game")
        break

    if user_input not in choices:
        print("Enter a valid choice [rock , paper , scissors] , Try Again")
        continue

    bot_input=random.choice(choices)
    print("Bot Choice : ",bot_input)
    if user_input == bot_input:
        print("It's a Tie")
    elif (user_input=="rock" and bot_input=="scissors") or (user_input=="scissors" and bot_input=="paper") or(user_input=="paper" and bot_input=="rock"):
        print("you win this round")
        user_points+=1
    else:
        print("Bot wins this round")
        bot_points+=1

    print(f"YOUR SCORE : {user_points} , BOT SCORE : {bot_points}") 