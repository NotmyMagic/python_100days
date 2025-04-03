from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUi:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text="Score: 0", font=("Ariel", 20 , "italic"), fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, text="The Question", fill=THEME_COLOR, font=("Ariel", 20 , "italic"), width=290)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_image = PhotoImage(file="./part4/gui_quiz_app/images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.test_true)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="./part4/gui_quiz_app/images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.test_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text=f"Quiz Finished! You got {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def test_true(self):
        check_answer = self.quiz.check_answer(True)
        self.user_feedback(check_answer)

    def test_false(self):
        check_answer = self.quiz.check_answer(False)
        self.user_feedback(check_answer)

    def user_feedback(self, checkanswer):
        if checkanswer == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_next_question)

