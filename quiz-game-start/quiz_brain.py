class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list #gets the list from main function
        self.counter = 0 #just counts the total score

    def next_question(self):
        current_question=self.questions_list[self.question_number]
        self.question_number+=1
        user_input=input(f"Q{self.question_number}. {current_question.Q_question} true/false? ")
        self.check_answer(user_input, current_question.Q_answer)
    def is_question(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False


    def check_answer(self,user_input,current_a):
        if user_input.lower()==current_a.lower():
            print("Correct!")
            self.counter+=1
        else :
            print("Wrong!")
        print(f"{self.counter}/{self.question_number}")