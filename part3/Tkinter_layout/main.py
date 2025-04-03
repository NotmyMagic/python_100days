from tkinter import *


window = Tk()
window.title("Tkinter works!")
window.minsize(width=500, height=400)

label = Label(text="The lable", font=("Ariel", 19 , "italic"))
label.grid(column=0, row=0, padx=15, pady=15)

# label["text"] = "Other Text"
# label.config(text="New Text")

# Button
def button_clicked():
    label["text"] = input.get()


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

btn2 = Button(text="hahaha")
btn2.grid(column=2, row=0)

#Entry

input = Entry(width=20)
input.grid(column=3, row=2)


# text = Text(width=50, height=3)
# text.pack()

# box = Spinbox()
# box.pack()

# scale = Scale()
# scale.pack(side="right")

# check = Checkbutton()
# check.pack()

# radio = Radiobutton()
# radio.pack()

# list = Listbox()
# list.pack()


window.mainloop()