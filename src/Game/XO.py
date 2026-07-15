import tkinter as tk
from tkinter import messagebox


class XOGame:

    def __init__(self, root):

        self.root = root
        self.root.title("XO Tic Tac Toe")
        self.root.geometry("450x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#202020")


        self.current_player = "X"

        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]


        self.buttons = []


        # ===== Title =====

        title = tk.Label(
            root,
            text="❌ TIC TAC TOE ⭕",
            font=("Arial", 26, "bold"),
            fg="white",
            bg="#202020"
        )

        title.pack(pady=20)



        # ===== Status =====

        self.status = tk.Label(
            root,
            text="Player X Turn",
            font=("Arial",18,"bold"),
            fg="yellow",
            bg="#202020"
        )

        self.status.pack()



        # ===== Board =====

        board_frame = tk.Frame(
            root,
            bg="#202020"
        )

        board_frame.pack(pady=30)



        for row in range(3):

            button_row = []

            for col in range(3):

                btn = tk.Button(
                    board_frame,
                    text="",
                    width=5,
                    height=2,
                    font=("Arial",32,"bold"),
                    bg="#333333",
                    fg="white",
                    command=lambda r=row,c=col:
                    self.play(r,c)
                )


                btn.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5
                )


                button_row.append(btn)


            self.buttons.append(button_row)



        # ===== Control Button =====

        control = tk.Frame(
            root,
            bg="#202020"
        )

        control.pack(pady=20)



        restart_btn = tk.Button(
            control,
            text="Restart",
            font=("Arial",15,"bold"),
            width=12,
            height=2,
            bg="#4CAF50",
            fg="white",
            command=self.restart
        )

        restart_btn.grid(
            row=0,
            column=0,
            padx=10
        )



        exit_btn = tk.Button(
            control,
            text="Exit",
            font=("Arial",15,"bold"),
            width=12,
            height=2,
            bg="#F44336",
            fg="white",
            command=root.destroy
        )


        exit_btn.grid(
            row=0,
            column=1,
            padx=10
        )




    # =====================
    # Player Click
    # =====================

    def play(self,row,col):

        if self.board[row][col] != "":
            return


        self.board[row][col] = self.current_player


        if self.current_player == "X":

            self.buttons[row][col].config(
                text="X",
                fg="#00FFFF"
            )

        else:

            self.buttons[row][col].config(
                text="O",
                fg="#FF5555"
            )



        if self.check_winner(self.current_player):

            self.status.config(
                text=f"Player {self.current_player} Wins!"
            )


            messagebox.showinfo(
                "Game Over",
                f"Player {self.current_player} Win!"
            )


            self.disable_buttons()

            return



        if self.check_draw():

            self.status.config(
                text="Draw Game"
            )


            messagebox.showinfo(
                "Game Over",
                "Draw!"
            )


            self.disable_buttons()

            return



        # Change player

        if self.current_player == "X":

            self.current_player="O"

        else:

            self.current_player="X"



        self.status.config(
            text=f"Player {self.current_player} Turn"
        )





    # =====================
    # Check Winner
    # =====================

    def check_winner(self,p):


        # Row

        for row in range(3):

            if (
                self.board[row][0]==p and
                self.board[row][1]==p and
                self.board[row][2]==p
            ):

                return True



        # Column

        for col in range(3):

            if (
                self.board[0][col]==p and
                self.board[1][col]==p and
                self.board[2][col]==p
            ):

                return True



        # Diagonal

        if (
            self.board[0][0]==p and
            self.board[1][1]==p and
            self.board[2][2]==p
        ):

            return True



        if (
            self.board[0][2]==p and
            self.board[1][1]==p and
            self.board[2][0]==p
        ):

            return True



        return False





    # =====================
    # Draw Check
    # =====================

    def check_draw(self):

        for row in self.board:

            for cell in row:

                if cell == "":

                    return False


        return True





    # =====================
    # Disable after finish
    # =====================

    def disable_buttons(self):

        for row in self.buttons:

            for btn in row:

                btn.config(
                    state="disabled"
                )





    # =====================
    # Restart
    # =====================

    def restart(self):

        self.current_player="X"


        self.board=[
            ["","",""],
            ["","",""],
            ["","",""]
        ]


        for row in self.buttons:

            for btn in row:

                btn.config(
                    text="",
                    state="normal",
                    fg="white"
                )


        self.status.config(
            text="Player X Turn"
        )






if __name__=="__main__":

    root=tk.Tk()

    game=XOGame(root)

    root.mainloop()