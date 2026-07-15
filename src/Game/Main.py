import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os


class GameMenu:

    def __init__(self, root):

        self.root = root

        self.root.title("Game Center")
        self.root.geometry("620x520")
        self.root.configure(bg="#202020")
        self.root.resizable(False, False)


        title = tk.Label(
            root,
            text="🎮 GAME CENTER 🎮",
            font=("Arial", 30, "bold"),
            fg="white",
            bg="#202020"
        )

        title.pack(pady=50)



        snake_button = tk.Button(
            root,
            text="🐍 Snake Game",
            font=("Arial",20),
            width=20,
            height=2,
            bg="#4CAF50",
            fg="white",
            command=self.open_snake
        )

        snake_button.pack(pady=15)



        xo_button = tk.Button(
            root,
            text="❌⭕ Tic Tac Toe (XO)",
            font=("Arial",20),
            width=20,
            height=2,
            bg="#2196F3",
            fg="white",
            command=self.open_xo
        )

        xo_button.pack(pady=15)



        exit_button = tk.Button(
            root,
            text="Exit",
            font=("Arial",15),
            width=12,
            command=root.destroy
        )

        exit_button.pack(pady=20)



    def run_game(self, filename):

        # หาตำแหน่งเดียวกับ main.py
        folder = os.path.dirname(os.path.abspath(__file__))

        game_path = os.path.join(
            folder,
            filename
        )


        if os.path.exists(game_path):

            subprocess.Popen(
                [sys.executable, game_path]
            )

        else:

            messagebox.showerror(
                "ไม่พบไฟล์",
                f"หาไฟล์ไม่เจอ:\n{game_path}"
            )



    def open_snake(self):

        self.run_game("snakegame.py")



    def open_xo(self):

        self.run_game("XO.py")





if __name__ == "__main__":

    root = tk.Tk()

    app = GameMenu(root)

    root.mainloop()