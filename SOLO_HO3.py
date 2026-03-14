import tkinter as tk

def add():
    try:
        a = float(e1.get())
        b = float(e2.get())
        result.config(text=f"Result: {a + b}")
    except:
        result.config(text="Invalid input")

def subtract():
    try:
        a = float(e1.get())
        b = float(e2.get())
        result.config(text=f"Result: {a - b}")
    except:
        result.config(text="Invalid input")

def multiply():
    try:
        a = float(e1.get())
        b = float(e2.get())
        result.config(text=f"Result: {a * b}")
    except:
        result.config(text="Invalid input")

def divide():
    try:
        a = float(e1.get())
        b = float(e2.get())
        result.config(text=f"Result: {a / b}")
    except ZeroDivisionError:
        result.config(text="Cannot divide by zero")
    except:
        result.config(text="Invalid input")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("360x230")
root.resizable(False, False)
result = tk.Label(root, text="Result will appear here.", font=("Arial", 11))
result.grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(root, text="Enter 1st Number:").grid(row=1, column=0, sticky="e", padx=8, pady=6)
tk.Label(root, text="Enter 2nd Number:").grid(row=2, column=0, sticky="e", padx=8, pady=6)
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=1, column=1, padx=8, pady=6)
e2.grid(row=2, column=1, padx=8, pady=6)
btn_frame = tk.Frame(root)
btn_frame.grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(btn_frame, text="Add", width=10, command=add).grid(row=0, column=0, padx=6, pady=6)
tk.Button(btn_frame, text="Subtract", width=10, command=subtract).grid(row=0, column=1, padx=6, pady=6)
tk.Button(btn_frame, text="Multiply", width=10, command=multiply).grid(row=1, column=0, padx=6, pady=6)
tk.Button(btn_frame, text="Division", width=10, command=divide).grid(row=1, column=1, padx=6, pady=6)
root.mainloop()
