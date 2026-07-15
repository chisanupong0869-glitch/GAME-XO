import tkinter as tk
from src.Game.XO import TicTacToe

def main():
    print("Starting XO Game...")
    
    # 1. สร้างหน้าต่างหลักของโปรแกรม
    root = tk.Tk()
    
    # 2. นำหน้าต่างหลักไปใส่ในคลาส TicTacToe ที่ import มา
    app = TicTacToe(root)
    
    # 3. สั่งให้โปรแกรมรันค้างไว้เพื่อแสดงหน้าต่าง GUI
    root.mainloop()

if __name__ == "__main__":
    main()