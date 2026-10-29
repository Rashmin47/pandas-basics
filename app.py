from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
my_label = Label(text="I Am a Label")
my_label.pack(side="left")
button= Button(text="Click Me")
button.pack()
window.mainloop()