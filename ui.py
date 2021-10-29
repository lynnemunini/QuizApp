from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("500x600")
        self.window.config(bg="white")

        # Header

        self.q_canvas = Canvas(width=64, height=64, bg="white", highlightthickness=0)
        self.q_image = PhotoImage(file="images/Q.png")
        self.q_canvas.create_image(32, 32, image=self.q_image)
        self.q_canvas.place(x=130, y=50)
        self.u_canvas = Canvas(width=64, height=64, bg="white", highlightthickness=0)
        self.u_image = PhotoImage(file="images/U.png")
        self.u_canvas.create_image(32, 32, image=self.u_image)
        self.u_canvas.place(x=200, y=50)
        self.i_canvas = Canvas(width=64, height=64, bg="white", highlightthickness=0)
        self.i_image = PhotoImage(file="images/I.png")
        self.i_canvas.create_image(32, 32, image=self.i_image)
        self.i_canvas.place(x=270, y=50)
        self.z_canvas = Canvas(width=64, height=64, bg="white", highlightthickness=0)
        self.z_image = PhotoImage(file="images/Z.png")
        self.z_canvas.create_image(32, 32, image=self.z_image)
        self.z_canvas.place(x=340, y=50)
        # self.z2_canvas = Canvas(width=64, height=64, bg="white", highlightthickness=0)
        # self.z2_image = PhotoImage(file="images/Z.png")
        # self.z2_canvas.create_image(32, 32, image=self.z2_image)
        # self.z2_canvas.place(x=310, y=50)
        # self.l_canvas = Canvas(width=64, height=64, bg="white", highlightthickness=0)
        # self.l_image = PhotoImage(file="images/L.png")
        # self.l_canvas.create_image(32, 32, image=self.l_image)
        # self.l_canvas.place(x=380, y=50)
        # self.e_canvas = Canvas(width=64, height=64, bg="white", highlightthickness=0)
        # self.e_image = PhotoImage(file="images/E.png")
        # self.e_canvas.create_image(32, 32, image=self.e_image)
        # self.e_canvas.place(x=450, y=50)
        # self.r_canvas = Canvas(width=64, height=64, bg="white", highlightthickness=0)
        # self.r_image = PhotoImage(file="images/R.png")
        # self.r_canvas.create_image(32, 32, image=self.r_image)
        # self.r_canvas.place(x=520, y=50)

        self.score = 0

        # Score
        self.score_label = Label(bg="white", highlightthickness=0, text="Score: 0",
                                 fg="black", font=("Courier", 15, "bold"))
        self.score_label.place(x=300, y=170)

        # Canvas with quiz
        self.quiz_canvas = Canvas(width=450, height=200, bg="white", highlightthickness=0)
        self.quiz_text = self.quiz_canvas.create_text(230, 100, text="", fill="black", width=400,
                                                      font=("Courier", 14, "normal"))
        self.quiz_canvas.place(x=25, y=200)

        # CheckMark
        check_image = PhotoImage(file="images/checkmark (1).png")
        self.check_image_button = Button(image=check_image, bg="white", highlightthickness=0, border=0, command=self.get_answer_true)
        self.check_image_button.place(x=70, y=410)

        # Cross
        cross_image = PhotoImage(file="images/cancel.png")
        self.cross_image_button = Button(image=cross_image, bg="white", highlightthickness=0, border=0, command=self.get_answer_false)
        self.cross_image_button.place(x=310, y=440)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.quiz_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.quiz_canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.quiz_canvas.itemconfig(self.quiz_text, text="You have completed the quiz!")
            # To disable the buttons
            self.check_image_button.config(state="disabled")
            self.cross_image_button.config(state="disabled")

    def get_answer_true(self):
        self.feedback(is_right=self.quiz.check_answer("True"))

    def get_answer_false(self):
        self.feedback(is_right=self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.quiz_canvas.config(bg="#C2F784")

        else:
            self.quiz_canvas.config(bg="#FF9292")

        self.window.after(1000, self.get_next_question)





