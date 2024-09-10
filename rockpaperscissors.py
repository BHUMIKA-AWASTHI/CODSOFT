import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock, Paper, Scissors")
        self.window.geometry("300x200")

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(self.window, text="Choose one of the following options:", font=("Arial", 12))
        self.label.pack()

        self.rock_button = tk.Button(self.window, text="Rock", command=lambda: self.play(1))
        self.rock_button.pack()

        self.paper_button = tk.Button(self.window, text="Paper", command=lambda: self.play(2))
        self.paper_button.pack()

        self.scissors_button = tk.Button(self.window, text="Scissors", command=lambda: self.play(3))
        self.scissors_button.pack()

        self.result_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.result_label.pack()

        self.score_label = tk.Label(self.window, text="Score: You - 0, Computer - 0", font=("Arial", 12))
        self.score_label.pack()

        self.play_again_button = tk.Button(self.window, text="Play Again", command=self.play_again)
        self.play_again_button.pack()

    def play(self, user_choice):
        computer_choice = random.randint(1, 3)

        if user_choice == 1:  # Rock
            if computer_choice == 1:
                result = "It's a tie!"
            elif computer_choice == 2:
                result = "Computer wins! Paper beats Rock."
                self.computer_score += 1
            else:
                result = "You win! Rock beats Scissors."
                self.user_score += 1
        elif user_choice == 2:  # Paper
            if computer_choice == 1:
                result = "You win! Paper beats Rock."
                self.user_score += 1
            elif computer_choice == 2:
                result = "It's a tie!"
            else:
                result = "Computer wins! Scissors beats Paper."
                self.computer_score += 1
        else:  # Scissors
            if computer_choice == 1:
                result = "Computer wins! Rock beats Scissors."
                self.computer_score += 1
            elif computer_choice == 2:
                result = "You win! Scissors beats Paper."
                self.user_score += 1
            else:
                result = "It's a tie!"

        self.result_label.config(text=f"User: {self.get_choice_name(user_choice)}, Computer: {self.get_choice_name(computer_choice)}\n{result}")
        self.score_label.config(text=f"Score: You - {self.user_score}, Computer - {self.computer_score}")

    def get_choice_name(self, choice):
        if choice == 1:
            return "Rock"
        elif choice == 2:
            return "Paper"
        else:
            return "Scissors"

    def play_again(self):
        self.result_label.config(text="")
        self.score_label.config(text=f"Score: You - {self.user_score}, Computer - {self.computer_score}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()