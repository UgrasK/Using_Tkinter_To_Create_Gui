from tkinter import *

# window
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()


# define a function and call it on button command to change label text
# def button_clicked():
#     my_label.config(text="button got clicked")

# define a function and call it on button command to change label text with input text
def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click me ", command=button_clicked)
button.pack()

# define an input field with Entry
input = Entry(width=10)
input.pack()










window.mainloop()