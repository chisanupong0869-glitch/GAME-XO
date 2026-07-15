import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe (XO)")
        self.root.geometry("400x520")
        self.root.configure(bg="#212121") # พื้นหลังสีเทาเข้ม
        self.root.resizable(False, False)

        self.player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        # --- ส่วนหัว (แสดงสถานะ) ---
        self.title_label = tk.Label(
            root, 
            text="Player X's Turn", 
            font=("Helvetica", 22, "bold"), 
            bg="#212121", 
            fg="#FFFFFF"
        )
        self.title_label.pack(pady=25)

        # --- ส่วนตารางเกม ---
        self.frame = tk.Frame(root, bg="#212121")
        self.frame.pack()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for row in range(3):
            for col in range(3):
                btn = tk.Button(
                    self.frame, 
                    text="", 
                    font=("Helvetica", 45, "bold"), 
                    width=3, height=1,
                    bg="#323232",           # สีปุ่ม
                    fg="#FFFFFF", 
                    activebackground="#424242", 
                    relief="flat",          # ทำให้ปุ่มแบนเรียบ ดูโมเดิร์น
                    command=lambda r=row, c=col: self.click(r, c)
                )
                btn.grid(row=row, column=col, padx=5, pady=5)
                self.buttons[row][col] = btn

        # --- ปุ่มเริ่มเกมใหม่ ---
        self.reset_btn = tk.Button(
            root, 
            text="Restart Game", 
            font=("Helvetica", 14, "bold"), 
            bg="#4CAF50",           # สีเขียว
            fg="white",
            activebackground="#45A049", 
            relief="flat", 
            width=15,
            command=self.reset
        )
        self.reset_btn.pack(pady=30)

    def click(self, row, col):
        # ถ้าช่องว่าง และยังไม่มีใครชนะ ให้สามารถกดได้
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.player
            
            # กำหนดสีให้ X และ O
            color = "#FF4C4C" if self.player == "X" else "#4CA6FF"
            self.buttons[row][col].config(text=self.player, fg=color)

            # ตรวจสอบผลลัพธ์หลังจากการกด
            if self.check_winner():
                self.title_label.config(text=f"Player {self.player} Wins! 🎉", fg="#FFD700") # สีทองเมื่อชนะ
                self.highlight_winner(color)
            elif self.check_draw():
                self.title_label.config(text="It's a Draw! 🤝", fg="#AAAAAA")
            else:
                # สลับผู้เล่น
                self.player = "O" if self.player == "X" else "X"
                self.title_label.config(text=f"Player {self.player}'s Turn", fg="#FFFFFF")

    def check_winner(self):
        # ตรวจสอบแนวนอนและแนวตั้ง
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "": 
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "": 
                return True
        
        # ตรวจสอบแนวทแยง
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "": 
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "": 
            return True
            
        return False

    def check_draw(self):
        for row in self.board:
            if "" in row: 
                return False
        return True

    def highlight_winner(self, color):
        # ทำให้ปุ่มที่ไม่ใช่ตัวชนะมีสีซีดลงนิดหน่อย (ลูกเล่นเพิ่มเติม)
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col]["text"] == "":
                    self.buttons[row][col].config(bg="#2A2A2A")

    def reset(self):
        # ล้างค่าทุกอย่างกลับไปเริ่มต้น
        self.player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.title_label.config(text="Player X's Turn", fg="#FFFFFF")
        
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="", bg="#323232")

# --- รันโปรแกรม ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()