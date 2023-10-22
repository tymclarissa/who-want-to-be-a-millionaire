from question_list import questions
from Question import Question
from QuestionMaster import QuestionMaster

question_bank= []
for question in questions:
    question_bank.append(Question(question["question"], question['answer']))

question_master = QuestionMaster(question_bank)
question_master.start_quiz()