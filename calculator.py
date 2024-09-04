import tkinter as tk

def calculate():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        else:
            result = "Error: Invalid operation"

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Error: Invalid input")

root = tk.Tk()
root.title("Simple Calculator")

num1_label = tk.Label(root, text="Number 1:")
num1_label.pack()

num1_entry = tk.Entry(root)
num1_entry.pack()

num2_label = tk.Label(root, text="Number 2:")
num2_label.pack()

num2_entry = tk.Entry(root)
num2_entry.pack()

operation_var = tk.StringVar()
operation_var.set("+")

operation_label = tk.Label(root, text="Operation:")
operation_label.pack()

operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()