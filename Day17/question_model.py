class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

new_question = Question("What is 2 into 2?", "4")
print(f"Question : {new_question.text} \n Answer: {new_question.answer}")