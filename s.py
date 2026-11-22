import tkinter as tk

win = tk.Tk()
win.geometry("500x500")
win.title("это мой первый проект")


def f():
    win.destroy()
    


label = tk.Label(win,font=("Arial",26),text="Рассмотри получше проект").grid(row=0,column=0,columnspan=4)
btn1= tk.Button(win,command=f,text="Жмакни на меня").grid(row=1,column=0,columnspan=2)

win.mainloop()