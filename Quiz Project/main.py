import question_model
import data
from quiz_brain import QuizBrain

question_bank= []
for i, obj in enumerate(data.question_data):
    text = data.question_data[i]['text']
    answer = data.question_data[i]['answer']
    question = question_model.Question(text, answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:    
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was {quiz.current_score}/{len(quiz.questions_list)}")

# for question in question_bank:
#     answer = input(f"Q{} bla bla: ")
#     quiz_brain = QuizBrain(question_bank,answer)
#     quiz_brain.next_question()
    