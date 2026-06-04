import string

 string.ascii_lowercase

 'abcdefghijklmnopqrstuvwxyz'

 a=list(string.ascii_lowercase)

 print(a)

 def encryption(text, encryption_number, choice):

     caesar_word=""

     if choice==1:

         for i in text:

             if i in a:

                 index=a.index(i)

                 index=(index+encryption_number)%26

                 caesar_word=caesar_word+a[index]

             else:

                 caesar_word=caesar_word+i

         return caesar_word

     elif choice==2:

         for i in text:

             if i in a:

                 index=a.index(i)

                 index=(index-encryption_number)%26

                 caesar_word=caesar_word+a[index]

             else:

                 caesar_word=caesar_word+i

         return caesar_word

     else:

         print("wrong input given :(")


 userInput1=input(str("enter the text ")).lower()

 userInput2=int(input("enter the encryption/decryption number "))

 userInput3=int(input("enter 1 for encrypt 2 for decrypt "))

 ans=encryption(userInput1, userInput2,userInput3)
 
print(ans)
 
