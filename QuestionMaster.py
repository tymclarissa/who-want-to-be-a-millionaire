from images import starting_image, win_image, lose_image
from Question import Question
from typing import List
import random

class QuestionMaster:
    def __init__(self, q_list: List[Question]):
        self.q_list = q_list
        self.q_number = 1
        self.score = 0

    def start_quiz(self):
        print(starting_image)
        while self.q_number <= 10:
            self.display_next_question()

        print(f"Quiz is over, you scored {self.score}")

        if (self.score > 5):
            print(win_image)
        else:
            print(lose_image)

    def display_next_question(self):  # listOfQn = [qn1, qn2, qn3]
        next_question = self.q_list[random.randint(0, len(self.q_list) - 1)]
        prompt = f"Q{self.q_number} - {next_question.question} (True or False): "
        user_answer = input(prompt)

        while user_answer != "True" and user_answer != "False":
            print()
            print("Type either True or False")
            user_answer = input(prompt)

        if bool(user_answer) == next_question.answer:
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!")

        self.q_number += 1
        print()
