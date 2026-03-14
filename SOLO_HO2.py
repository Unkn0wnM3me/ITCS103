import tkinter as tk

root = tk.Tk()
root.title("Student Profile")
root.geometry("600x600")
root.resizable(False, True)
root.configure(bg="#ffd6e0")

title = tk.Label(root, text="Student Profile", font=("Helvetica", 32, "bold"), bg="#ffd6e0")
title.pack(pady=20)

frame = tk.Frame(root, bg="#ffd6e0")
frame.pack(fill="both", expand=True, padx=40)

tk.Label(frame, text="Name : Ken Gimelson B. Solo", font=("Helvetica", 16), bg="#ffd6e0", anchor="w", justify="left").pack(anchor="w", pady=8)
tk.Label(frame, text="Age : 18 years old", font=("Helvetica", 16), bg="#ffd6e0", anchor="w", justify="left").pack(anchor="w", pady=8)
tk.Label(frame, text="Course : BSIT", font=("Helvetica", 16), bg="#ffd6e0", anchor="w", justify="left").pack(anchor="w", pady=8)
tk.Label(frame, text="Birthday : May 28, 2007", font=("Helvetica", 16), bg="#ffd6e0", anchor="w", justify="left").pack(anchor="w", pady=8)
tk.Label(frame, text="Motto :", font=("Helvetica", 16), bg="#ffd6e0", anchor="w", justify="left").pack(anchor="w", pady=(20,4))
tk.Label(frame, text="Start small. Keep learning.", font=("Helvetica", 14, "italic"), bg="#ffd6e0", wraplength=520, anchor="w", justify="left").pack(anchor="w")

root.mainloop()
