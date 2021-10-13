from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# my_label = Label()
# my_label.grid(column=0, row=0)

input = Entry(width=7)
input.grid(column=1, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=1)

equal = Label(text="is equal to", )
equal.grid(column=0, row=2)

km = Label(text="0")
km.grid(column=1, row=2)

def convert():
    mile_num = int(input.get())
    result = float(mile_num * 1.609)
    result = round(result, 2)
    km.config(text=result)

km_label = Label(text="Km")
km_label.grid(column=2, row=2)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=3)

window.mainloop()