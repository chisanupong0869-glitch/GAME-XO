import tkinter as tk
import random

WIDTH = 600
HEIGHT = 600
SPACE_SIZE = 20
BODY_PARTS = 3
SPEED = 120

BACKGROUND_COLOR = "#111111"
SNAKE_COLOR = "#00FF66"
FOOD_COLOR = "#FF3333"
TEXT_COLOR = "white"

class Snake:

    def __init__(self):

        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(BODY_PARTS):
            self.coordinates.append([0,0])

        for x,y in self.coordinates:
            square = canvas.create_rectangle(
                x,y,
                x+SPACE_SIZE,
                y+SPACE_SIZE,
                fill=SNAKE_COLOR,
                outline="#00aa44"
            )
            self.squares.append(square)


class Food:

    def __init__(self):

        x = random.randint(0,(WIDTH//SPACE_SIZE)-1)*SPACE_SIZE
        y = random.randint(0,(HEIGHT//SPACE_SIZE)-1)*SPACE_SIZE

        self.coordinates = [x,y]

        canvas.create_oval(
            x,y,
            x+SPACE_SIZE,
            y+SPACE_SIZE,
            fill=FOOD_COLOR,
            outline=""
        )


def next_turn(snake, food):

    global direction
    global score

    x,y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x,y))

    square = canvas.create_rectangle(
        x,y,
        x+SPACE_SIZE,
        y+SPACE_SIZE,
        fill=SNAKE_COLOR,
        outline="#00aa44"
    )

    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        score += 1
        score_label.config(text="Score : {}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):

        game_over()

    else:

        window.after(SPEED,next_turn,snake,food)


def change_direction(new_direction):

    global direction

    if new_direction=="left":
        if direction!="right":
            direction=new_direction

    elif new_direction=="right":
        if direction!="left":
            direction=new_direction

    elif new_direction=="up":
        if direction!="down":
            direction=new_direction

    elif new_direction=="down":
        if direction!="up":
            direction=new_direction


def check_collisions(snake):

    x,y = snake.coordinates[0]

    if x <0 or x>=WIDTH:
        return True

    if y<0 or y>=HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:

        if x==body_part[0] and y==body_part[1]:
            return True

    return False


def game_over():

    canvas.delete(tk.ALL)

    canvas.create_text(
        WIDTH/2,
        HEIGHT/2-30,
        font=("Arial",40,"bold"),
        text="GAME OVER",
        fill="red"
    )

    canvas.create_text(
        WIDTH/2,
        HEIGHT/2+20,
        font=("Arial",20),
        text=f"Final Score : {score}",
        fill="white"
    )

    restart_btn = tk.Button(
        window,
        text="Play Again",
        font=("Arial",15),
        bg="#00aa44",
        fg="white",
        command=restart_game
    )

    canvas.create_window(WIDTH/2,HEIGHT/2+80,window=restart_btn)


def restart_game():

    global score
    global direction

    canvas.delete("all")

    score = 0
    direction = "down"

    score_label.config(text="Score : 0")

    snake = Snake()
    food = Food()

    next_turn(snake,food)


def start_game():

    start_btn.destroy()

    snake = Snake()

    food = Food()

    next_turn(snake,food)


window = tk.Tk()

window.title("Snake Game")

window.resizable(False,False)

score = 0
direction = "down"

title = tk.Label(
    window,
    text="🐍 SNAKE GAME",
    font=("Arial",26,"bold"),
    fg="#00FF66",
    bg="#222222"
)

title.pack(fill="x")

score_label = tk.Label(
    window,
    text="Score : 0",
    font=("Arial",18),
    fg="white",
    bg="#222222"
)

score_label.pack(fill="x")

canvas = tk.Canvas(
    window,
    bg=BACKGROUND_COLOR,
    height=HEIGHT,
    width=WIDTH,
    highlightthickness=0
)

canvas.pack()

start_btn = tk.Button(
    window,
    text="START GAME",
    font=("Arial",18,"bold"),
    bg="#00aa44",
    fg="white",
    padx=20,
    pady=10,
    command=start_game
)

start_btn.pack(pady=15)

window.bind("<Left>",lambda event:change_direction("left"))
window.bind("<Right>",lambda event:change_direction("right"))
window.bind("<Up>",lambda event:change_direction("up"))
window.bind("<Down>",lambda event:change_direction("down"))

window.mainloop()