
from art import logo, vs
from famous_personality import famous_people_instagram
print("lower higher \n")

print(logo)
import random




# print(len(famous_people_instagram))

#print(famous_people_instagram.keys())

a = random.choice(list(famous_people_instagram.keys()))

b = random.choice(list(famous_people_instagram.keys()))

while a==b:
    b = random.choice(list(famous_people_instagram.keys()))

user_input = str(input("do you wanna play higher or lower game, 'y' or 'n'?  "))

while user_input == 'y':
    score = 0
    play=True

    while play:

        print(a)

        print(vs)

        print(b)

        HL = str(input("H or L")).lower()

        if HL == 'l':

            if famous_people_instagram[b]["followers"] > famous_people_instagram[a]["followers"]:

                print("correct \n")

                score += 1
                a=b
                b=random.choice(list(famous_people_instagram.keys()))

            else:

                print("wrong\n")
                print(a,famous_people_instagram[a])
                print(b,famous_people_instagram[b])
                print("score is: ", score)
                play=False

        if HL=='h':

            if famous_people_instagram[b]["followers"] < famous_people_instagram[a]["followers"]:
                print("correct \n")

                score += 1
                a = b
                b = random.choice(list(famous_people_instagram.keys()))

            else:

                print("wrong\n")
                print(a,famous_people_instagram[a])
                print(b,famous_people_instagram[b])
                print("score is: ", score)
                play=False

    user_input=str(input("do you wanna try the game again, 'y' or 'n'?  "))
