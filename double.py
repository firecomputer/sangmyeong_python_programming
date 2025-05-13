from tkinter import *
window = Tk()
photo1 = PhotoImage(file = "C:\Users\jaeyo\Downloads\happy cat.gif")
photo2 = PhotoImage(file = "C:\Users\jaeyo\Downloads\lights.gif")

label1 = Label(window, image = photo1)
label2 = Label(window, image = photo2)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop() 
