from question_model import Questions
from data import question_data2
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data2:
    question= Questions(i["question"],i["correct_answer"])
    question_bank.append(question)
#print(question_bank[4].Q_question, question_bank[4].Q_answer)
quiz_brain = QuizBrain(question_bank)
while quiz_brain.is_question():
    quiz_brain.next_question()
    #quiz_brain.check_answer()

