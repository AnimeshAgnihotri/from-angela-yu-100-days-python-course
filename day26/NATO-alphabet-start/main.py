student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key, value)
#     pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(index, row)
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# klkl={index: row for index, row in student_data_frame.iterrows()}
# print(klkl)
nato_df=pandas.read_csv("nato_phonetic_alphabet.csv")

#print(nato_dict)
#TODO 1. Create a dictionary in
# this format:
{"A": "Alfa", "B": "Bravo"}




nato_dict1 = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(nato_dict1)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please enter your choice: ")
user_input_split = user_input.split()
phonetic_dict=[word:nat_word for (word, nat_word) in nato_dict1.items() if word in user_input_split]

