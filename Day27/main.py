from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)



my_label = Label(text="I am a label")
my_label.pack()

my_label.config(text="New Text")

new_input = Entry(width=10)
new_input.pack()


def button_clicked():
    value_entered = new_input.get()
    my_label.config(text=value_entered)

my_button = Button(text="Click Me", command=button_clicked)
my_button.pack()



window.mainloop()