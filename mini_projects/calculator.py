import tkinter as tk

root = tk.Tk()
root.title("Python Calculator")

root.geometry("400x550")
root.resizable(False, False)

display = tk.Entry(
    root,
    font=("Arial", 24),
    borderwidth=5,
    relief="ridge",
    justify="right"
)
display.grid(row=0, column=0, columnspan=4, padx=15, pady=20, ipady=20)

def on_button_click(value):
    display.insert(tk.END, value)

def on_clear():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        result = eval(expression)

        on_clear()
        display.insert(0, str(result))
    except Exception:     
        on_clear()
        display.insert(tk.END, "Error")


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), width=5, height=2 , command=calculate if text == "=" else lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

clear_btn = tk.Button(
    root,
    text="C",
    font=("Arial", 18),
    width=22,
    height=2,
    bg="tomato",
    command=on_clear
)

clear_btn.grid(
    row=5,
    column=0,
    columnspan=4,
    padx=5,
    pady=5
)
    



root.mainloop()