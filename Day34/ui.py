THEME_COLOR = "#375362"
DEFAULT_SCORE = 0

from tkinter import * 
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizier")
        self.window.config(bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {DEFAULT_SCORE}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(pady=20, column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(padx=20, pady=20, column=0, row=1, columnspan=2)

        self.canvas_text = self.canvas.create_text(150, 125,width=270, text="Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))

        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0)
        self.right_button.grid(pady=20, column=0, row=2)

        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0)
        self.wrong_button.grid(pady=20, column=1, row=2)

        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text, text=q_text)