from tkinter import Tk, Label, Button, mainloop
from threading import Thread
import time


class App(Tk):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="")
        self.label.pack()

        button = Button(self, text="Да")
        button.config(command=self.print)
        button.pack()
        button2 = Button(self, text="Нет")
        button2.config(command=self.print)
        button2.pack()
        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.after(1000, self.update_clock)
    def print(self):
        def thread():
            while True:
                print("Поток безконечный цикл")
                time.sleep(1)
        Thread(target=thread).start()