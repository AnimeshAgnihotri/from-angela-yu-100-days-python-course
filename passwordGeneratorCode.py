
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-','@']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
import random

password=[]
#list shuffle makes sure we dont pick only the starting of the list elements
for i in letters:
    if len(password)==nr_letters:
        break
    password.append(letters[random.randint(0,len(letters)-1)])
for i in numbers:
    if len(password)==nr_numbers+nr_letters:
        break
    password.append(numbers[random.randint(0,len(numbers)-1)])
for i in symbols:
    if len(password)==nr_symbols+nr_numbers+nr_letters:
        break
    password.append(symbols[random.randint(0,len(symbols)-1)])
random.shuffle(password)
ans=""
for i in password:
    ans=ans+i
print(ans)

