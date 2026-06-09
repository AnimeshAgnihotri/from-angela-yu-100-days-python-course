from logos import logo_1
import random
#*************************************************************************************************
E=5
H=5
print(logo_1)
num_list=[random.randint(1,100)]
#for i in range(1,101):
   # num_list.append(i)
#print(num_list)
chosen_number=random.choice(num_list)
#print(chosen_number)

#*************************************************************************************************
def guess_Func(chosen_number, chance):
    while chance != 0:
        chance = chance - 1
        guess = int(input("guess the number: "))

        print(chosen_number)
        if guess < chosen_number:
            print("you guessed the number low")
            print(f"chance left: {chance}")
        elif guess == chosen_number:
            print("you guessed the number\n")
            break

        else:
            print("you guessed the number high")
            print(f"chance left: {chance}")
#*************************************************************************************************
def game(user_choice):
    while user_choice!="n":
        if user_choice not in ["y","n"]:
            break
        level = input(str("what difficulty you want easy or hard? "))
        if level == "easy":
            chance = E
        else:
            chance = H

        guess_Func(chosen_number, chance)

        user_choice=input(str("*****do wanna guess a number type 'y' or  'n'__ "))

#**************************************************************************************************
a=str(input("do you wanna start this game? type 'y' or  'n'__ "))
if a=='y':
    user_choice = input(str("*****do wanna guess a number? type 'y' or  'n'__ "))
    game(user_choice)
