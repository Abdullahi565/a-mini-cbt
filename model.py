from datetime import datetime

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class CBT:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.current_index = 0
        self.start_time = datetime.now()

    def add_question(self, question):
        self.questions.append(question)

    def get_current_question(self):
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def answer_question(self, user_answer):
        question = self.get_current_question()
        if question and question.check_answer(user_answer):
            self.score += 1
        self.current_index += 1

    def get_result(self):
        end_time = datetime.now()
        return {
            "score": self.score,
            "total": len(self.questions),
            "time": end_time.strftime("%Y-%m-%d %H:%M:%S")
        }