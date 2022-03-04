from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in range(len(question_data)):
    new_q = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score is {quiz.score}/{quiz.question_number}")