
import tkinter as tk
import random
def play_round(player_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(player_choice, computer_choice)
    result_label.config(text=f"You chose: {player_choice}\nComputer chose: {computer_choice}\n{result}")
def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("1000x1000")
root.title("Rock, Paper, Scissors")
rock_button = tk.Button(root, text="Rock",width=10, command=lambda: play_round("rock"))
rock_button.pack(pady=5)
paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_round("paper"))
paper_button.pack(pady=5)
scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_round("scissors"))
scissors_button.pack(pady=5)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)
root.mainloop()