import random

rock = "o"
paper = "[]"
scissors = "=<"

choice = [rock, paper, scissors]

cpu_choice = random.randint(0, 2)
player_choice = int(input("Rock is 1, paper is 2, and scissors is 3\n"))

# player choice | cpu choice
# 1|3  Win
# 3|2  Win
# 2|1  Win


if player_choice >= 1 and player_choice <= 3:
    print(choice[player_choice -1])

if player_choice <= 0 or player_choice >= 4:
    print("invalid Number")
elif cpu_choice == player_choice -1:
    print(choice[cpu_choice])
    print("Its a draw")
elif cpu_choice == 2 and player_choice -1 == 0:
    print(choice[cpu_choice])
    print("you Win")
elif cpu_choice == 0 and player_choice -1 == 2:
    print(choice[cpu_choice])
    print("you Lose")
elif cpu_choice < player_choice -1:
    print(choice[cpu_choice])
    print("you Win")
elif cpu_choice > player_choice -1:
    print(choice[cpu_choice])
    print("you Lose")
else:
    print("What do you mean thats not even close to what I said!?")


# if cpu_choice == 1 and player_choice == 1:
#     print("the computer chose Rock "+ str(cpu_choice))
#     print("it's a draw")

# elif cpu_choice == 1 and player_choice == 2:
#     print("the computer chose Rock "+ str(cpu_choice))
#     print("You Win")

# elif cpu_choice == 1 and player_choice == 3:
#     print("the computer chose Rock "+ str(cpu_choice))
#     print("You Lose")

# elif cpu_choice == 2 and player_choice == 1:
#     print("the computer chose Rock "+ str(cpu_choice))
#     print("You Lose")

# elif cpu_choice == 2 and player_choice == 2:
#     print("the computer chose Rock "+ str(cpu_choice))
#     print("It's a draw")

# elif cpu_choice == 2 and player_choice == 3:
#     print("the computer chose Rock "+ str(cpu_choice))
#     print("You Win")

# elif cpu_choice == 3 and player_choice == 1:
#     print("the computer chose Rock "+ str(cpu_choice))
#     print("You Win")

# elif cpu_choice == 3 and player_choice == 2:
#     print("the computer chose Rock "+ str(cpu_choice))
#     print("You Lose")

# elif cpu_choice == 3 and player_choice == 3:
#     print("the computer chose Rock "+ str(cpu_choice))
#     print("It's a draw")
    
# else:
#     print("Not a valid choice")