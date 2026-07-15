import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os


class GameMenu:

    def __init__(self, root):

        self.root = root
        self.root.title("Game Center")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#222222")


        title = tk.Label(
            root,
            text="🎮 GAME CENTER 🎮",
            font=("Arial", 24, "bold"),
            fg="white",
            bg="#222222"
        )
        title.pack(pady=50)


        snake_btn = tk.Button(
            root,
            text="🐍 Snake Game",
            font=("Arial", 16, "bold"),
            width=20,
            height=2,
            bg="#4CAF50",
            fg="white",
            command=self.open_snake
        )

        snake_btn.pack(pady=20)



        xo_btn = tk.Button(
            root,
            text="❌⭕ Tic Tac Toe",
            font=("Arial", 16, "bold"),
            width=20,
            height=2,
            bg="#2196F3",
            fg="white",
            command=self.open_xo
        )

        xo_btn.pack(pady=20)



        exit_btn = tk.Button(
            root,
            text="Exit",
            font=("Arial", 16),
            width=20,
            height=2,
            bg="#F44336",
            fg="white",
            command=root.destroy
        )

        exit_btn.pack(pady=20)



    def run_game(self, filename):

        # ตำแหน่งของ Menu.py
        folder = os.path.dirname(os.path.abspath(__file__))

        game_path = os.path.join(folder, filename)


        # ตรวจสอบไฟล์
        if not os.path.exists(game_path):

            messagebox.showerror(
                "File not found",
                f"ไม่พบไฟล์:\n{game_path}"
            )

            return


        try:

            subprocess.Popen(
                [sys.executable, game_path]
            )


        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )



    def open_snake(self):

        self.run_game("snakegame.py")



    def open_xo(self):

        self.run_game("XO.py")





if __name__ == "__main__":

    root = tk.Tk()

    app = GameMenu(root)

    root.mainloop()