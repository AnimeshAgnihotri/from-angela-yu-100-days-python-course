import random
from logos import logo_2
print(logo_2)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card_addition=0
comp_addition=0
#user_card=[]
#computer_card=[]
def computer_card_add(computer_card,comp_addition):
    summ=comp_addition
    for i in computer_card:
        summ+=i
    return summ

def user_card_add(user_card, card_addition):
    #card_addition=0
    summ=card_addition
    for i in user_card:
        summ+=i
    return summ




user_input=input(str("do you wanna play the blackjack game 'y' or 'n' \n"))
while user_input == "y":

    user_card=[]
    computer_card=[]
    user_card.append(random.choice(cards))
    user_card.append(random.choice(cards))
    print(f"user cards are {user_card} \n")
    computer_card.append(random.choice(cards))
    computer_card.append(random.choice(cards))
    print(f"computer card is {computer_card[0]} \n")
    user_card_input = input(str("do you wanna draw card\n 'y' or 'n'"))



    while user_card_input == 'y'or  user_card_input=='n':
        card_addition = user_card_add(user_card, card_addition)
        if user_card_input == 'y':
            user_card.append(random.choice(cards))

            #computer_card.append(random.choice(cards))


        if user_card_input=='n':
            #card_addition =computer_card_add(computer_card)

            while comp_addition<16:
                computer_card.append(random.choice(cards))
                comp_addition=computer_card_add(computer_card, comp_addition)
            break
        #print(f"{comp_addition}= comp_addition")
        if card_addition>21:
            break
        print(f"{card_addition} =card_addition")
        print(f"user cards are {user_card} \n")
        #print(f"computer card is {computer_card}")
        user_card_input = input(str("do you wanna draw card\n 'y' or 'n'"))



    if card_addition==21 and comp_addition==21:
        print("draw ")
        print(f"{comp_addition}= comp_addition")
        print(f"{card_addition} =card_addition")
        print(f"user cards are {user_card} \n")
        print(f"computer card is {computer_card} \n")

    elif card_addition==21:
        print("you win")
        print(f"{comp_addition}= comp_addition")
        print(f"{card_addition} =card_addition")
        print(f"user cards are {user_card} \n")
        print(f"computer card is {computer_card} \n")

    elif card_addition>21:
        print("you lose")
        print(f"{comp_addition}= comp_addition")
        print(f"{card_addition} =card_addition")
        print(f"user cards are {user_card} \n")
        print(f"computer card is {computer_card} \n")
    elif comp_addition>21:
        print("you win")
        print(f"{comp_addition}= comp_addition")
        print(f"{card_addition} =card_addition")
        print(f"user cards are {user_card} \n")
        print(f"computer card are {computer_card} \n")
    else:
        print("you lose")
        print(f"{card_addition} =card_addition")
        print(f"user cards are {user_card} \n")
        print(f"computer card is {computer_card} \n")





    user_input=input(str("do you wanna play the blackjack game\n 'y' or 'n'))"))

print("you selected no\n *********")
