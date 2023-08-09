from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import random
import string


def generatePassword():
    name = name_entry.get()
    alphabets = string.ascii_letters
    alpha_digits = string.digits
    special_char = string.punctuation

    combined_char = alphabets+alpha_digits+special_char
    no_of_char = int(charBox.get())

    if choice.get()==1:
        pass_field.insert(0, random.sample(alphabets, no_of_char))
    elif choice.get()==2:
        pass_field.insert(0, random.sample(alphabets+alpha_digits, no_of_char))
    else:
        pass_field.insert(0, random.sample(combined_char, no_of_char))
    
    show_message(f" {name}, your password has been generated! ")

def clear_text():
    pass_field.delete(0,END)

def show_message(message):
    messagebox.showinfo("Password Generator", message)

root = Tk()
root.title("Password Generator")
root.geometry("600x600")
root.resizable(False,False)

choice = IntVar()
choice.set(None)

my_font = Font(
    family='ravie',
    size=20,
    weight='bold',
)

frame1 = Frame(root, bg="#C576F6")
frame1.pack(side=TOP, fill="x")
label = Label(frame1, text="Password Generator", fg="white", bg="#C576F6", font=my_font)
label.pack(pady=50)


frame2 = LabelFrame(root, text="Enter Your Name")
frame2.pack(pady=20)

name_entry = Entry(frame2, font="lucida 10")
name_entry.pack(pady=20, padx=80, ipadx=50)

frame2 = LabelFrame(root, text="Number of Password Characters?")
frame2.pack(pady=20)

charBox = Spinbox(frame2, from_=5, to=20, width=14, font="lucida 12")
charBox.pack(pady=20, padx=80, ipadx=50)

weak_radioButton = Radiobutton(root, text="Weak", value=1, variable=choice, font='lucida 10', command=clear_text)
weak_radioButton.place(x=150, y=380)

medium_radioButton = Radiobutton(root, text="Medium", value=2, variable=choice, font='lucida 10', command=clear_text)
medium_radioButton.pack()

strong_radioButton = Radiobutton(root, text="Strong", value=3, variable=choice, font='lucida 10', command=clear_text)
strong_radioButton.place(x=375, y=380)

generate_button = Button(root, text="Generate", font="ravie 12", bg="#C576F6", fg="white", relief="flat", command=generatePassword)
generate_button.place(x=245, y=420)

pass_field = Entry(root, bd=2, width=25, font="lucida 10")
pass_field.pack(pady=70, padx=80, ipadx=30)

root.mainloop()
