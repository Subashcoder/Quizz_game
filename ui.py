from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UserInterface:
    
    def __init__(self, quizzclass: QuizBrain):
        self.quiz = quizzclass
        self.score = self.quiz.score
        self.window = Tk()
        self.window.title("Quizz Game Interface")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        
        self.score_text = Label(text=f"score:{self.score}")
        self.score_text.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, background='white')
        self.question_label = self.canvas.create_text(150, 125,width=250, text="Question section", font=('Arial', 20, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20,pady=20)
        
        self.right_image = PhotoImage(file='./images/true.png')
        self.false_image = PhotoImage(file='./images/false.png')
        
        self.right_button = Button(image=self.right_image, command=self.button_true)
        self.right_button.grid(column=0, row=2) 
        
        self.wrong_button = Button(image=self.false_image, command=self.button_false)
        self.wrong_button.grid(column=1, row=2) 
        
        self.display_question()
        
        self.window.mainloop()
        
    def display_question(self):
        if self.quiz.still_has_questions():
            question = self.quiz.next_question()
            self.score_text.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfigure(self.question_label, text= question)
            self.canvas.configure(background='white')
        else:
            self.canvas.itemconfigure(self.question_label, text = f'You have answer all the question.\nFinal Score: {self.quiz.score}/10')
            self.right_button.configure(state='disabled')
        
        
    def button_true(self):
        is_true = self.quiz.check_answer('true')
        self.givefeedback(is_true)
        
        
    def button_false(self):
        is_true = self.quiz.check_answer('false')
        self.givefeedback(is_true)
        
        
    def givefeedback(self, is_true):
        if is_true:
            self.canvas.configure(background='green')
            self.window.after(1000, func=self.display_question)
        else:
            self.canvas.configure(background='red')
            self.window.after(1000, func=self.display_question)
            
        

