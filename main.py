from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for i in question_data:
    question= Questions(i["text"],i["answer"])
    question_bank.append(question)
#print(question_bank[4].Q_question, question_bank[4].Q_answer)
quiz_brain = QuizBrain(question_bank)
while quiz_brain.is_question():
    quiz_brain.next_question()
    #quiz_brain.check_answer()

