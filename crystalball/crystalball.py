# -*- coding: utf-8 -*-

'''
A simple crystal ball app 
Author: AFA 
'''

from PIL import Image, ImageTk
import random
import itertools as it

try:
    import Tkinter as tk # Python 2.7
except ImportError:
    import tkinter as tk  # Python 3

LANG = [
    "FR",
    "JP",
    "EN"
]

ASK = [
    'DEMANDER',
    '尋ねる', # Tazuneru
    'ASK'
]

EXIT = [
    'SORTIE',
    '出口',  # Deguchi
    'EXIT'
]   

ANSWERS_EN = [
    'Yes',
    'No',
    'Ask again later',
    "Maybe?",
    "Not sure",
    '50/50'
]

ANSWERS_FR = [
    'Oui',
    'Non',
    'Demander plus tard',
    'Peut être',
    'Pas certain',
    '50/50'
]

ANSWERS_JP = [
    'はい',
    'いいえ',
    '後でもう一度尋ねる',
    '多分?',
    'わからない',
    '50/50'
]

''' 
ANSWERS_JP2 = [
    'Hai',
    'Iie',
    'Atode mōichido tazuneru',
    'Tabun?',
    'Wakaranai',
    '50/50'
] 
'''

class App(object):
    def __init__(self, master):

        # Main frame 
        frame = tk.Frame(master)
        frame.pack()
        self.f = frame

        # Secondary frame
        f2 = tk.Frame(master)
        f2.place(relx=1, rely=0, anchor=tk.NE)

        # Crystal ball image
        try:
            image = Image.open("image/crystalball.jpg") # image from Amazon.com
        except IOError:
            pass
        image = image.resize((400,400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        # Crystal ball image Label
        self.crystal_ball = tk.Label(frame, image=photo)
        self.crystal_ball.image = photo
        self.crystal_ball.pack()

        # Answer Text | Label
        self.answer_text = tk.StringVar()
        self.answer = tk.Label(frame, font=("Verdana", 16), textvariable=self.answer_text)
        self.answer.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Ask Button
        self.ask_button = tk.Button(frame, text="ASK", highlightbackground="green", width=9, command=self.get_answer)
        self.ask_button.pack(side=tk.LEFT)

        # Exit Button
        self.exit_button = tk.Button(frame, text="EXIT", highlightbackground="red", width=9, command=frame.quit)
        self.exit_button.pack(side=tk.RIGHT)

        # Language choice | Button
        self.languages = it.cycle(LANG)
        self.ask_lang = it.cycle(ASK)
        self.exit_lang = it.cycle(EXIT)

        self.lang_button = tk.Button(frame, text="EN", highlightbackground="aqua", command=self.toggle_lang)
        self.lang_button.pack()

        # Dark | Light mode | Button
        self.mode = it.cycle(["L", "D"])
        self.color_mode = tk.Button(f2, text="D", width=2, command=self.toggle_mode)
        self.color_mode.pack(side=tk.LEFT)
    

    # Method to get answer depending on language choice
    def get_answer(self):
        # if self.lang_button['text'] == LANG[0]:
        #     self.english()
        # elif self.lang_button['text'] == LANG[1]:
        #     self.french()
        # else:
        #     self.japanese()
        check = self.lang_button['text']
        self.english() if check == "EN" else self.french() if check == "FR" else self.japanese()


    # Different language options 
    def english(self):
        self.answer_text.set(random.choice(ANSWERS_EN))


    def french(self):
        self.answer_text.set(random.choice(ANSWERS_FR))


    def japanese(self):
        self.answer_text.set(random.choice(ANSWERS_JP))
        

    # Method to toggle betweeen languages
    def toggle_lang(self):
        self.lang_button['text'] = next(self.languages)
        self.ask_button['text'] = next(self.ask_lang)
        self.exit_button['text'] = next(self.exit_lang)


    # Method to toggle between dark | light mode 
    def toggle_mode(self):
        self.color_mode['text'] = next(self.mode)
        self.light_mode() if self.color_mode['text'] == "D" else self.dark_mode()


    # Method to set light mode 
    def light_mode(self):
        self.color_mode.config(highlightbackground="white")
        self.ask_button.config(highlightbackground="green")
        self.exit_button.config(highlightbackground="red")
        self.lang_button.config(highlightbackground="aqua")
        self.f.config(bg="white")
        root.config(bg="white")
    

    # Method to set dark mode 
    def dark_mode(self):
        self.color_mode.config(highlightbackground="black")
        self.ask_button.config(highlightbackground="black")
        self.exit_button.config(highlightbackground="black")
        self.lang_button.config(highlightbackground="black")
        self.f.config(bg="black")
        root.config(bg="black")

# end of class 
    
root = tk.Tk()
app = App(root)
root.title("Crystal Ball")          # Window title 
root.geometry("450x440+200+200")    # Window size   
root.mainloop()
root.destroy()
