from tkinter import *
from tkinter.font import Font
import tkinter as tk


def onButtonPress(event):
    global value
    text = event.widget.cget("text")

    if text == "=":
        if value.get().isdigit():
            entry_val = int(value.get())
        else:
            try:
                entry_val = eval(screen_entry.get())
            except Exception as e:
                print(e)
                value.set("Error")
                screen_entry.update()

        value.set(entry_val)
        screen_entry.update()

    elif text == "C":
        value.set("")
        screen_entry.update()
    
    elif text == ".":
        if not screen_entry.get():
            screen_entry.insert(tk.END, "0.")
        elif "." not in screen_entry.get():
            screen_entry.insert(tk.END, ".")
    
    elif text == "%":
        try:
            expression = screen_entry.get()
            result = eval(expression) / 100
            screen_entry.delete(0, tk.END)
            screen_entry.insert(tk.END, str(result))
        except Exception as e:
            screen_entry.delete(0, tk.END)
            screen_entry.insert(tk.END, "Error")

    else:
        value.set(value.get() + text)
        screen_entry.update()


root = Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(False,False)
root.configure(bg="#d8f9ff")


value = StringVar()
value.set("")
calc_font = Font(
    family='lucida',
    size=30,
    weight='normal',
)
screen_entry = Entry(root, textvar=value, font=calc_font,
                     relief='sunken', highlightthickness=1, borderwidth=2)
screen_entry.pack(fill=X, ipadx=8, pady=10, padx=10)

button_symbols = [
    [("C", (18, 15)), (".", (23, 15)), ("/", (23, 15)), ("%", (17, 15))],
    [("7", (20, 15)), ("8", (20, 15)), ("9", (20, 15)), ("*", (23, 15))],
    [("4", (20, 15)), ("5", (20, 15)), ("6", (20, 15)), ("-", (23, 15))],
    [("1", (20, 15)), ("2", (20, 15)), ("3", (20, 15)), ("+", (20, 15))],
    [("0", (121, 15)), ("=", (20, 15))]
]

for row_symbols in button_symbols:
    box = tk.Frame(root, bg='#d8f9ff')
    box.pack(fill=tk.BOTH)

    for symbol, (padx, pady) in row_symbols:
        button = tk.Button(box, text=symbol, padx=padx, pady=pady,
                           font="lucida 20", bg='teal', relief='raised', fg="white")
        button.pack(side=tk.LEFT, padx=12, pady=10)
        button.bind("<ButtonPress>", onButtonPress)

root.mainloop()
