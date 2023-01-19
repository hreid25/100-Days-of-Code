import question_model
import data

question_bank= []
for i, obj in enumerate(data.question_data):
    text = data.question_data[i]['text']
    answer = data.question_data[i]['answer']
    question = question_model.Question(text, answer)
    question_bank.append(question)

print(question_bank[0].answer)