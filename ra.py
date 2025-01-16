from tkinter import Tk, Label, Button, mainloop
from threading import Thread
import time, os, sys


class App(Tk):
    def __init__(self, sec=0):
        super().__init__()
        self.second=sec
        self.geometry("200x100+500+500")
        self.title("Удаление!")
        self.label = Label(self, text="")
        self.label.pack()

        button = Button(self, text="Удалить всё из папок")
        button.config(command=lambda: self.delete_path("GGG"))
        button.pack()

        self.update_clock()


    def update_clock(self):
        if (self.second==0):
            self.delete_path("GGG")
            quit()

        now = time.strftime("0:0:"+str(self.second))
        self.label.configure(text=now)
        self.second-=1
        self.after(1000, self.update_clock)
    def print(self):
        def thread():
            while True:
                print("Поток безконечный цикл")
                time.sleep(1)
        Thread(target=thread).start()

    def delete_path(self, path_):
        #print("поехали")

        for root, dirs, files in os.walk(path_, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))

def main():
    arg = sys.argv
    #print(len(arg),arg)
    if (len(arg)==3):
        app = App(int(arg[2]))
        app.mainloop()
    else:
        app=App(0)
        app.mainloop()



if __name__ == '__main__':
    main()