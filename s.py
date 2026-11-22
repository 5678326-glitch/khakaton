import tkinter as tk

win = tk.Tk()


def p():
    win1=tk.Toplevel(win)
    win1.geometry("500x500")
    win1.title("это мой second проект")
    win.withdraw()

win.geometry("500x500")
win.title("это мой первый проект")


def f():
    win.destroy()
    


label = tk.Label(win,font=("Arial",26),text="Рассмотри получше проект").grid(row=0,column=0,columnspan=4)
btn1= tk.Button(win,command=f,text="Жмакни на меня").grid(row=1,column=0,columnspan=2)
btn= tk.Button(win,command=p,text="Жмакни на меня nkll").grid(row=2,column=0,columnspan=2)


win.mainloop()