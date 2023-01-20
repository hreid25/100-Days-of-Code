# ask the questions
# check answer was correct
# are we at end of the quiz?

class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.current_score = 0
    
    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q:{self.question_number}: {current_question.text} (True/False)?: ")
        self.answer_correct(user_answer, current_question.answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
    
    def answer_correct(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.current_score += 1
            print("Congrats, you got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.current_score}/{self.question_number}")
        print("\n")

# Question format: "Q.1: question text True/False?: "