import numpy as np
import random
import tkinter as tk
from tkinter import ttk, simpledialog

class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quadratic Equation Game")
        self.root.geometry("400x300")

        self.label = ttk.Label(self.root, text="", font=('Helvetica', 14))
        self.label.pack(pady=10)

        self.generate_button = ttk.Button(self.root, text="Start", command=self.generate_and_display)
        self.generate_button.pack(pady=10)

        self.entry = ttk.Entry(self.root, font=('Helvetica', 12))
        self.entry.pack(pady=10)

        self.submit_button = ttk.Button(self.root, text="Enter", command=self.choose_option)
        self.submit_button.pack(pady=10)

        self.skip_button = ttk.Button(self.root, text="Skip Turn", command=self.skip_turn)
        self.skip_button.pack(pady=10)

        self.result_label = ttk.Label(self.root, text="", font=('Helvetica', 12))
        self.result_label.pack(pady=10)

        self.scores = [0, 0]  # Initialize scores here

    def generate_and_display(self):
        self.generate_equation()
        equation_text = f"The quadratic equation with roots is: 1x^2 + ({-self.roots[0] + -self.roots[1]})x + {self.roots[0] * self.roots[1]} = 0"
        self.label.config(text=equation_text)

    def generate_equation(self):
        numbers = np.arange(1, 21)
        self.roots = np.random.choice(numbers, 2, replace=False)
        self.diff = abs(self.roots[0] - self.roots[1])
        self.options = random.sample(self.roots.tolist(), len(self.roots))

    def choose_option(self):
        player = self.scores.index(max(self.scores))
        user_input = self.entry.get().upper()

        if user_input == 'A':
            choice = self.options[0]
        elif user_input == 'B':
            choice = self.options[1]
        else:
            self.result_label.config(text="Invalid input. Enter 'A' or 'B'")
            return

        self.process_choice(player, choice)
        self.generate_and_display()  # Automatically regenerate equation after the turn

    def skip_turn(self):
        skip_choice = simpledialog.askstring("Skip Turn", "Is the other player willing to skip? (Enter 'yes' or 'no')")
        if skip_choice and skip_choice.lower() == 'yes':
            self.process_choice(0, -1)  # Player 1 skips the turn
            self.generate_and_display()  # Automatically regenerate equation after the turn
        player = self.scores.index(max(self.scores))
        score_text = f"The turn is skipped \n Player {player+1} should play"
        self.result_label.config(text=score_text)


    def process_choice(self, player, choice):
        if choice == max(self.roots):
            self.scores[player] += self.diff
        elif choice == -1:
            pass  # Skip turn, no scores
        else:
            self.scores[1 - player] += self.diff
        player = self.scores.index(max(self.scores))
        score_text = f"The scores are: Player 1 - {self.scores[0]}, Player 2 - {self.scores[1]} \n Player {player+1} should play"
        self.result_label.config(text=score_text)

        if max(self.scores) >= 100:
            self.result_label.config(text=f"Player {player + 1} wins!")

    def play(self):
        self.root.mainloop()

game = Game()
game.play()
