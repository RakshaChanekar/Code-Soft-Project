import random
item_list = ["Rock","Paper","Scissor"]

user_choice = input("Enter your move o= Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice ={user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paprt covers Rock = computer win")
    else:
        print("Rock smashes Scissor = You win")

elif user_choice == "Paper":
   if comp_choice == "Scissor":
       print("Scissir cuts paper, Computer Win")
   else:
       print("Paper covers rock, you win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You win")
    else:
        print("Rock smashes scissor, Computer win")
