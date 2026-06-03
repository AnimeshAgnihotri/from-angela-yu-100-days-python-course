#code coming in 
word_list=["laptop", "phone", "office"]

import random

random_choice=random.choice(word_list)

print(random_choice)
 
runtime=len(random_choice)
 
#placeholder=""

#for i in random_choice:

   # placeholder=placeholder+"._. "

   # print(placeholder)

#print(placeholder)

wordList=[]

display=[" _ "]*len(random_choice)

print(display)

while runtime>0:

    guess=input(str("enter your guess: "))


    if guess in random_choice:

        if guess in wordList:

            print("already guessed")

            continue

            #display=display+guess


        else:

            wordList.append(guess)

            print("correct")

            for i in range (len(random_choice)):

                if random_choice[i]==guess:

                    display[i]=guess



    else:

        print("wrong")

         # continue

    runtime=runtime-1

print(" ".join(display)) 

print(display)

if(" _ " not in display):

    print("you won")

else:

    print("lost")
 
