import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_words = {}

# get word bank
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_list = original_data.to_dict(orient="records")
else:
    # list of dictionaries with French: french word, English: english_word
    word_list = data.to_dict(orient="records")


# -------------------------- Flash Card Mechanisms -------------------------- #


def next_card():
    global flip_timer, current_words
    window.after_cancel(flip_timer)
    current_words = random.choice(word_list)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_words["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_words["English"], fill="white")


def correct():
    word_list.remove(current_words)
    words_to_learn = pandas.DataFrame(word_list)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# -------------------------- UI -------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
canvas_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=correct)
right_button.grid(row=1, column=1)

flip_timer = window.after(1, next_card)

window.mainloop()
