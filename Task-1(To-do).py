import tkinter as tk
from tkinter import messagebox

def animate_title():
    colors = ["#ff006e", "#8338ec", "#3a86ff", "#00f5d4", "#ffbe0b"]
    current = title.cget("fg")
    next_color = colors[(colors.index(current) + 1) % len(colors)] if current in colors else colors[0]
    title.config(fg=next_color)
    root.after(300, animate_title)

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, "🟡 " + task)
        entry.delete(0, tk.END)
        update_count()
    else:
        messagebox.showwarning("Oops!", "Type something!")

def delete_task():
    try:
        listbox.delete(listbox.curselection())
        update_count()
    except:
        messagebox.showwarning("Oops!", "Select a task!")

def mark_done():
    try:
        i = listbox.curselection()[0]
        task = listbox.get(i)
        listbox.delete(i)
        listbox.insert(i, "🟢 " + task[2:])
    except:
        messagebox.showwarning("Oops!", "Select a task!")

def update_count():
    count_label.config(text=f"Tasks: {listbox.size()}")

# Window
root = tk.Tk()
root.title("To-Do App")
root.geometry("500x650")
root.configure(bg="#1b1b3a")

# Title
title = tk.Label(
    root,
    text="🌈 To-Do 🌈",
    font=("Comic Sans MS", 22, "bold"),
    bg="#1b1b3a",
    fg="#ff006e"
)
title.pack(pady=20)

# Entry
entry = tk.Entry(
    root,
    font=("Comic Sans MS", 14),
    width=28,
    bg="#fff",
    fg="#000",
    bd=3,
    relief="ridge"
)
entry.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#1b1b3a")
btn_frame.pack(pady=10)

def make_btn(text, color, cmd):
    return tk.Button(
        btn_frame,
        text=text,
        bg=color,
        fg="white",
        font=("Comic Sans MS", 12, "bold"),
        width=10,
        bd=0,
        command=cmd
    )

make_btn("➕ Add", "#3a86ff", add_task).grid(row=0, column=0, padx=6)
make_btn("✅ Done", "#00f5d4", mark_done).grid(row=0, column=1, padx=6)
make_btn("🗑 Delete", "#ff006e", delete_task).grid(row=0, column=2, padx=6)

# Listbox
listbox = tk.Listbox(
    root,
    font=("Comic Sans MS", 13),
    width=35,
    height=14,
    bg="#f1faee",
    fg="#1d3557",
    selectbackground="#8338ec",
    bd=3,
    relief="ridge"
)
listbox.pack(pady=20)

# Counter
count_label = tk.Label(
    root,
    text="Tasks: 0",
    font=("Comic Sans MS", 12, "bold"),
    bg="#1b1b3a",
    fg="white"
)
count_label.pack()

animate_title()
root.mainloop()

