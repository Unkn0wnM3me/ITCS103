import tkinter as tk
from tkinter import messagebox
from datetime import datetime

root = tk.Tk()
root.title("Profile Builder")
root.geometry("650x320")
root.resizable(False, False)

current_bg = "#8ee98a"
root.configure(bg=current_bg)

gender_var = tk.StringVar(value="Male")

main_frame = tk.Frame(root, bg=current_bg, bd=2, relief="ridge")
main_frame.place(x=10, y=45, width=630, height=180)

title_label = tk.Label(root, text="Profile Builder", font=("Times New Roman", 18, "bold"), bg=current_bg)
title_label.place(x=250, y=8)

first_entry = tk.Entry(main_frame, font=("Arial", 11))
middle_entry = tk.Entry(main_frame, font=("Arial", 11))
last_entry = tk.Entry(main_frame, font=("Arial", 11))
birth_entry = tk.Entry(main_frame, font=("Arial", 11), width=20)

first_label = tk.Label(main_frame, text="First Name", font=("Arial", 10, "italic"), bg=current_bg)
middle_label = tk.Label(main_frame, text="Middle Name", font=("Arial", 10, "italic"), bg=current_bg)
last_label = tk.Label(main_frame, text="Last Name", font=("Arial", 10, "italic"), bg=current_bg)
birth_label = tk.Label(main_frame, text="Birth Year", font=("Arial", 10, "italic"), bg=current_bg)
age_text_label = tk.Label(main_frame, text="Computing Age...", font=("Arial", 16, "italic"), bg=current_bg)
age_value_label = tk.Label(main_frame, text="", font=("Arial", 10, "bold"), bg=current_bg)
gender_label = tk.Label(main_frame, text="Gender", font=("Arial", 10, "italic"), bg=current_bg)

male_radio = tk.Radiobutton(
    main_frame,
    text="Male",
    variable=gender_var,
    value="Male",
    command=lambda: change_gender_color()
)

female_radio = tk.Radiobutton(
    main_frame,
    text="Female",
    variable=gender_var,
    value="Female",
    command=lambda: change_gender_color()
)

first_entry.place(x=10, y=10, width=195)
middle_entry.place(x=215, y=10, width=195)
last_entry.place(x=420, y=10, width=195)

first_label.place(x=55, y=40)
middle_label.place(x=255, y=40)
last_label.place(x=475, y=40)

birth_entry.place(x=10, y=50, width=195)
birth_label.place(x=55, y=80)

gender_label.place(x=55, y=106)

male_radio.place(x=230, y=104)
female_radio.place(x=320, y=104)

age_text_label.place(x=320, y=58)
age_value_label.place(x=385, y=92)

submit_button = tk.Button(
    root,
    text="Submit",
    font=("Arial", 12, "bold"),
    bg="#d9d9d9",
    activebackground="#c0c0c0",
    activeforeground="black",
    relief="raised",
    bd=3,
    width=10,
    command=lambda: submit_form()
)
submit_button.place(x=295, y=245)

def change_gender_color():
    global current_bg
    if gender_var.get() == "Male":
        current_bg = "#8ee98a"
    else:
        current_bg = "#f8b6c8"

    root.configure(bg=current_bg)
    main_frame.configure(bg=current_bg)
    title_label.configure(bg=current_bg)
    first_label.configure(bg=current_bg)
    middle_label.configure(bg=current_bg)
    last_label.configure(bg=current_bg)
    birth_label.configure(bg=current_bg)
    age_text_label.configure(bg=current_bg)
    age_value_label.configure(bg=current_bg)
    gender_label.configure(bg=current_bg)
    male_radio.configure(bg=current_bg)
    female_radio.configure(bg=current_bg)

def compute_age(event=None):
    year_text = birth_entry.get().strip()

    if not year_text.isdigit():
        age_value_label.config(text="")
        age_text_label.config(text="Computing Age...")
        return

    year = int(year_text)
    current_year = datetime.now().year
    age = current_year - year

    if age < 0:
        age_value_label.config(text="")
        age_text_label.config(text="Computing Age...")
        return

    age_text_label.config(text="Age")
    age_value_label.config(text=f"{age} years old")

def hover_on(event):
    submit_button.config(bg="#bfbfbf", relief="sunken")

def hover_off(event):
    submit_button.config(bg="#d9d9d9", relief="raised")

def submit_form():
    first = first_entry.get().strip()
    middle = middle_entry.get().strip()
    last = last_entry.get().strip()
    birth = birth_entry.get().strip()

    if first == "" or middle == "" or last == "" or birth == "":
        messagebox.showerror("Error", "Please fill out all fields.")
        return

    if not birth.isdigit():
        messagebox.showerror("Error", "Please enter a valid birth year.")
        return

    current_year = datetime.now().year
    age = current_year - int(birth)

    if age < 0:
        messagebox.showerror("Error", "Birth year cannot be greater than the current year.")
        return

    age_value_label.config(text=f"{age} years old")
    age_text_label.config(text="Age")

    card = tk.Toplevel(root)
    card.title("Student ID")
    card.geometry("300x200")
    card.resizable(False, False)
    card.configure(bg="#f6d2dd")

    card_frame = tk.Frame(card, bg="#e9ecff", bd=2, relief="ridge")
    card_frame.place(x=10, y=10, width=280, height=180)

    title = tk.Label(card_frame, text="Student ID", font=("Times New Roman", 16, "bold"), bg="#e9ecff")
    title.place(x=80, y=5)

    canvas = tk.Canvas(card_frame, width=70, height=70, bg="#e9ecff", highlightthickness=0)
    canvas.place(x=20, y=35)
    canvas.create_oval(10, 5, 60, 55, fill="#0c6798", outline="#0c6798")
    canvas.create_oval(25, 20, 45, 40, fill="#e9ecff", outline="#e9ecff")
    canvas.create_oval(18, 38, 52, 60, fill="#e9ecff", outline="#e9ecff")

    fullname = f"{first} {middle} {last}"
    gender = gender_var.get()

    name_label = tk.Label(card_frame, text=f"Name:   {fullname}", font=("Arial", 10), bg="#e9ecff", anchor="w")
    age_label = tk.Label(card_frame, text=f"Age:     {age} years old", font=("Arial", 10), bg="#e9ecff", anchor="w")
    gen_label = tk.Label(card_frame, text=f"Gender:  {gender}", font=("Arial", 10), bg="#e9ecff", anchor="w")

    name_label.place(x=10, y=115)
    age_label.place(x=10, y=135)
    gen_label.place(x=10, y=155)

    card.transient(root)
    card.grab_set()

birth_entry.bind("<Return>", compute_age)
submit_button.bind("<Enter>", hover_on)
submit_button.bind("<Leave>", hover_off)

change_gender_color()

root.mainloop()
