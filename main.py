# Importing the tkinter and ttk modules
from tkinter import *
from tkinter import ttk

# Setting up the main app
root = Tk()
root.title("Calculator")

# The frame for the calculator
frame = ttk.Frame(root, padding=10)
frame.grid()

# Label to be displayed at the top
label = Label(frame, text="Simple Calculator")
label.grid(column=0, row=0, columnspan=4)

# The entry widget where values will be displayed
text = StringVar()
display = Entry(frame, textvariable=text, font=('Arial', '15'))
display.grid(column=0, row=1, columnspan=4)


# Data entry button to be called once a button is pressed
def data_entry(value):
    display.insert(index=len(display.get()), string=str(value))


# Function to clear the values on the screen. To be called when clear button is pressed
def clear():
    display.delete(0, len(display.get()))


# Function to perform arithmetic operations when equals sign is pressed
def calculation():
    try:
        result = str(eval(display.get()))
        clear()
        display.insert(index=0, string=str(result))
    except:
        clear()
        display.insert(index=0, string="Error!")


# Buttons to be displayed as well as their respective commands and grid positions
cube = Button(frame, text="^3", height=3, width=6, command=lambda: data_entry("**3"))
cube.grid(column=0, row=2)

square = Button(frame, text="^2", height=3, width=6, command=lambda: data_entry("**2"))
square.grid(column=1, row=2)

square_root = Button(frame, text=" √ ", height=3, width=6, command=lambda: data_entry("**0.5"))
square_root.grid(column=2, row=2)

clear_button = Button(frame, text=" C ", height=3, width=6, command=clear)
clear_button.grid(column=3, row=2)

button_0 = Button(frame, text=" 0 ", height=3, width=6, command=lambda: data_entry(0))
button_0.grid(column=1, row=6)

button_1 = Button(frame, text=" 1 ", height=3, width=6, command=lambda: data_entry(1))
button_1.grid(column=0, row=5)

button_2 = Button(frame, text=" 2 ", height=3, width=6, command=lambda: data_entry(2))
button_2.grid(column=1, row=5)

button_3 = Button(frame, text=" 3 ", height=3, width=6, command=lambda: data_entry(3))
button_3.grid(column=2, row=5)

button_4 = Button(frame, text=" 4 ", height=3, width=6, command=lambda: data_entry(4))
button_4.grid(column=0, row=4)

button_5 = Button(frame, text=" 5 ", height=3, width=6, command=lambda: data_entry(5))
button_5.grid(column=1, row=4)

button_6 = Button(frame, text=" 6 ", height=3, width=6, command=lambda: data_entry(6))
button_6.grid(column=2, row=4)

button_7 = Button(frame, text=" 7 ", height=3, width=6, command=lambda: data_entry(7))
button_7.grid(column=0, row=3)

button_8 = Button(frame, text=" 8 ", height=3, width=6, command=lambda: data_entry(8))
button_8.grid(column=1, row=3)

button_9 = Button(frame, text=" 9 ", height=3, width=6, command=lambda: data_entry(9))
button_9.grid(column=2, row=3)

divide = Button(frame, text=" / ", height=3, width=6, command=lambda: data_entry("/"))
divide.grid(column=3, row=3)

multiply = Button(frame, text=" * ", height=3, width=6, command=lambda: data_entry("*"))
multiply.grid(column=3, row=4)

plus = Button(frame, text=" + ", height=3, width=6, command=lambda: data_entry("+"))
plus.grid(column=3, row=5)

minus = Button(frame, text=" - ", height=3, width=6, command=lambda: data_entry("-"))
minus.grid(column=3, row=6)

point = Button(frame, text=" . ", height=3, width=6, command=lambda: data_entry("."))
point.grid(column=0, row=6)

equals = Button(frame, text=" = ", height=3, width=6, command=calculation)
equals.grid(column=2, row=6)

# The application main loop to run until app is closed
root.mainloop()
