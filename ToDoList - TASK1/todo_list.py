from tkinter import *
from PIL import Image, ImageTk
from tkinter.font import Font
from tkinter import messagebox
import tkinter as tk

def taskEntry(event):
    task_entry.config(highlightcolor='#FC6C85')
    task_entry.config(highlightthickness=2)

def show_message(message):
    messagebox.showinfo("Task Submitted", message)

def add_task():
    task = task_entry.get()
    if task:

        task_entry.delete(0, tk.END)
        task_entry.config(highlightcolor='gray')
        task_entry.config(highlightthickness=1)

        selected_index = task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task_listbox.delete(index)
            task_listbox.insert(index, task)
            task_listbox.itemconfig(tk.END, {'bg':'#FF9999'})
        else:
            task_listbox.insert(tk.END, task)
            task_listbox.itemconfig(tk.END, {'bg':'#FF9999'})

        show_message(f"Task '{task}' submitted successfully!")

def edit_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        current_task = task_listbox.get(selected_index)
        task_entry.delete(0, tk.END)
        task_entry.insert(0, current_task)
        task_listbox.itemconfig(tk.END, {'bg':'#FF9999'})

def delete_task():
    selected_index = task_listbox.curselection()
    if selected_index:
        task_listbox.delete(selected_index)

root = Tk()
root.title("ToDoList")
root.geometry("480x650")
root.resizable(False,False)


my_font = Font(
    family='ravie',
    size=30,
    weight='bold',
)

frame1 = Frame(root, bg="#FC6C85")
frame1.pack(side=TOP, fill="x")
label = Label(frame1, text="ToDo List", fg="white", bg="#FC6C85", font=my_font)
label.pack(pady=50)  

frame2 = Frame(root, width=480,height=50,bg="white")
frame2.place(x=0,y=180)

my_task = StringVar()
task_entry = tk.Entry(frame2, width=24, font="lucida 20", bd=0, highlightcolor='gray', highlightthickness=1)
task_entry.place(x=9,y=7)
task_entry.bind('<FocusIn>', taskEntry)
task_entry.bind('<FocusOut>', lambda event: task_entry.config(highlightthickness=1))


button1 = Button(frame2, text="Submit", font="lucida 20", width=6, bg="#FC6C85", fg="white", bd=0, relief='raised', command=add_task)
button1.place(x=380,y=0)

frame3 = Frame(root, bd=1, width=480, height=280, bg='white')
frame3.pack(pady=(100,0))

task_listbox = Listbox(frame3, font="lucida 12", width=60, height=15)
task_listbox.pack(side=LEFT, fill=BOTH, padx=2)

delete_button = PhotoImage(file="delete.png")
Button(root, image=delete_button,bd=0, command=delete_task).place(x=250, y=577)

edit_button = Button(root, text="Edit", font="lucida 15", bg="#FF6863", fg="white", relief="flat", command=edit_task)
edit_button.place(x=170, y=584)

root.mainloop()


