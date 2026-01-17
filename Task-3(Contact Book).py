import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# ========== THEME ==========
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

# ========== DATABASE ==========
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    email TEXT,
    address TEXT
)
""")
conn.commit()

# ========== APP ==========
app = ctk.CTk()
app.geometry("390x700")
app.title("Cute Contact Book 💖")

# ========== HEADER ==========
header = ctk.CTkFrame(app, height=60, fg_color="#ffb6c1", corner_radius=0)
header.pack(fill="x")

title = ctk.CTkLabel(header, text="💖 My Contacts", font=("Comic Sans MS", 22, "bold"), text_color="white")
title.pack(pady=15)

# ========== MAIN ==========
main_frame = ctk.CTkFrame(app, corner_radius=20, fg_color="#fff0f5")
main_frame.pack(expand=True, fill="both", padx=10, pady=10)

def clear_main():
    for widget in main_frame.winfo_children():
        widget.destroy()

# ========== HOME ==========
def home_screen():
    clear_main()
    ctk.CTkLabel(main_frame, text="Welcome 🌸", font=("Comic Sans MS", 20, "bold")).pack(pady=30)
    ctk.CTkLabel(main_frame, text="Your cute contact manager 💕", font=("Comic Sans MS", 14)).pack()

# ========== ADD CONTACT ==========
def add_contact_screen():
    clear_main()

    ctk.CTkLabel(main_frame, text="Add New Contact 🌼", font=("Comic Sans MS", 20, "bold")).pack(pady=20)

    name_entry = ctk.CTkEntry(main_frame, placeholder_text="Name", width=260)
    phone_entry = ctk.CTkEntry(main_frame, placeholder_text="Phone", width=260)
    email_entry = ctk.CTkEntry(main_frame, placeholder_text="Email", width=260)
    address_entry = ctk.CTkEntry(main_frame, placeholder_text="Address", width=260)

    name_entry.pack(pady=8)
    phone_entry.pack(pady=8)
    email_entry.pack(pady=8)
    address_entry.pack(pady=8)

    def save_contact():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()

        if name == "" or phone == "":
            messagebox.showerror("Oops!", "Name & Phone are required 💢")
            return

        cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)",
                       (name, phone, email, address))
        conn.commit()

        messagebox.showinfo("Saved 💖", "Contact Added Successfully!")

        name_entry.delete(0, "end")
        phone_entry.delete(0, "end")
        email_entry.delete(0, "end")
        address_entry.delete(0, "end")

    ctk.CTkButton(main_frame, text="💾 Save Contact", fg_color="#ff69b4", command=save_contact).pack(pady=20)

# ========== SHOW CONTACTS ==========
def show_contacts():
    clear_main()
    ctk.CTkLabel(main_frame, text="My Cute Contacts 🧸", font=("Comic Sans MS", 20, "bold")).pack(pady=10)

    scroll = ctk.CTkScrollableFrame(main_frame, width=330, height=450)
    scroll.pack(pady=10)

    cursor.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()

    for row in rows:
        cid, name, phone, email, address = row

        card = ctk.CTkFrame(scroll, corner_radius=15, fg_color="#ffe4e1")
        card.pack(fill="x", pady=8, padx=5)

        ctk.CTkLabel(card, text=f"👤 {name}", font=("Comic Sans MS", 15, "bold")).pack(anchor="w", padx=10, pady=2)
        ctk.CTkLabel(card, text=f"📞 {phone}", font=("Comic Sans MS", 13)).pack(anchor="w", padx=10)

# ========== DEFAULT ==========
home_screen()

# ========== BOTTOM NAV ==========
bottom_nav = ctk.CTkFrame(app, height=70, fg_color="#ffb6c1", corner_radius=0)
bottom_nav.pack(fill="x", side="bottom")

btn_home = ctk.CTkButton(bottom_nav, text="🏠 Home", width=90, fg_color="#ff69b4", command=home_screen)
btn_add = ctk.CTkButton(bottom_nav, text="➕ Add", width=90, fg_color="#ff69b4", command=add_contact_screen)
btn_contacts = ctk.CTkButton(bottom_nav, text="📇 Contacts", width=90, fg_color="#ff69b4", command=show_contacts)

btn_home.pack(side="left", padx=10, pady=15)
btn_add.pack(side="left", padx=10)
btn_contacts.pack(side="left", padx=10)

app.mainloop()
