from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Calculator")

frame = ttk.Frame(root, padding=10)
frame.grid()

text = StringVar()
display = Entry(frame, textvariable=text)
display.grid(column=0, row=0, columnspan=4)


def data_entry(value):
    display.insert(index=len(display.get()), string=str(value))


button_0 = Button(frame, text=" 0 ", command=lambda: data_entry(0))
button_0.grid(column=1, row=4)

button_1 = Button(frame, text=" 1 ", command=lambda: data_entry(1))
button_1.grid(column=0, row=3)

button_2 = Button(frame, text=" 2 ", command=lambda: data_entry(2))
button_2.grid(column=1, row=3)

button_3 = Button(frame, text=" 3 ", command=lambda: data_entry(3))
button_3.grid(column=2, row=3)

button_4 = Button(frame, text=" 4 ", command=lambda: data_entry(4))
button_4.grid(column=0, row=2)

button_5 = Button(frame, text=" 5 ", command=lambda: data_entry(5))
button_5.grid(column=1, row=2)

button_6 = Button(frame, text=" 6 ", command=lambda: data_entry(6))
button_6.grid(column=2, row=2)

button_7 = Button(frame, text=" 7 ", command=lambda: data_entry(7))
button_7.grid(column=0, row=1)

button_8 = Button(frame, text=" 8 ", command=lambda: data_entry(8))
button_8.grid(column=1, row=1)

button_9 = Button(frame, text=" 9 ", command=lambda: data_entry(9))
button_9.grid(column=2, row=1)

divide = Button(frame, text=" / ", command=lambda: data_entry("/"))
divide.grid(column=3, row=1)

multiply = Button(frame, text=" * ", command=lambda: data_entry("*"))
multiply.grid(column=3, row=2)

plus = Button(frame, text=" + ", command=lambda: data_entry("+"))
plus.grid(column=3, row=3)

minus = Button(frame, text=" - ", command=lambda: data_entry("-"))
minus.grid(column=3, row=4)

point = Button(frame, text=" . ", command=lambda: data_entry("."))
point.grid(column=0, row=4)

equals = Button(frame, text=" = ")
equals.grid(column=2, row=4)


def typed_data(*args):
    print(display.get())


text.trace_add("write", typed_data)

root.mainloop()
