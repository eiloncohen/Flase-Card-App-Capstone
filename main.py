from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
FULL_FRONT_IMG_PATH = "C:/Users/eilon/PycharmProjects/Flase-Card-App-Capstone/images/card_front.png"
FULL_BACK_IMG_PATH = "C:/Users/eilon/PycharmProjects/Flase-Card-App-Capstone/images/card_back.png"
FULL_WRONG_IMG_PATH = "C:/Users/eilon/PycharmProjects/Flase-Card-App-Capstone/images/wrong.png"
FULL_CHECK_IMG_PATH = "C:/Users/eilon/PycharmProjects/Flase-Card-App-Capstone/images/right.png"
FULL_CSV_FILE_PATH = "C:/Users/eilon/PycharmProjects/Flase-Card-App-Capstone/data/french_words.csv"
FULL_WORDS_TO_LEARN_CSV_FILE_PATH = "C:/Users/eilon/PycharmProjects/Flase-Card-App-Capstone/data/words_to_learn.csv"

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv(FULL_WORDS_TO_LEARN_CSV_FILE_PATH)
except FileNotFoundError:
    original_data = pandas.read_csv(FULL_CSV_FILE_PATH)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(card_title, text='English', fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv(FULL_WORDS_TO_LEARN_CSV_FILE_PATH, index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=FULL_FRONT_IMG_PATH)
card_back_img = PhotoImage(file=FULL_BACK_IMG_PATH)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

cross_img = PhotoImage(file=FULL_WRONG_IMG_PATH)
unknown_button = Button(image=cross_img, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file=FULL_CHECK_IMG_PATH)
known_button = Button(image=check_img, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()
