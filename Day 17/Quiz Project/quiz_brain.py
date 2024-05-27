# TODO : asking the questions
# TODO : checking if the answer was correct
# TODO : checking if we're the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
