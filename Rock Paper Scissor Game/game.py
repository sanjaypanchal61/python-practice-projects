import random
item_list = ["rock","paper","scissor"]

user_choice = input("Enter your move: Rock, Paper, Scissor = ").lower()
comp_choice = random.choice(item_list)

if user_choice not in item_list:
    print("Invalid choice!")
    exit()

print(f"User choice = {user_choice} | Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Match Tie")

elif user_choice == "rock":
    if comp_choice == "paper":
        print("Paper covers Rock , Computer win")
    else:
        print("Rock smashes Scissor , You win")

elif user_choice == "paper":
    if comp_choice == "scissor":
        print("Scissor cuts Paper , Computer win")
    else:
        print("Paper covers Rock , You win")

elif user_choice == "scissor":
    if comp_choice == "paper":
        print("Scissor cuts Paper , You win")
    else:
        print("Rock smashes Scissor , Computer win")
      