from tkinter import *

FONT = ("Arial", 14, "bold")


# placing widgets: pack, place, grid.
# you can't mix up grid and pack.

def miles_to_km():
    # converting miles to km
    new_value = round(float(entry.get()) * 1.60934, 2)
    value_label.config(text=f"{new_value}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(padx=15, pady=15)

# Label 1
equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

# Label 2
value_label = Label(text="0", font=FONT)
value_label.grid(column=1, row=1)
value_label.config(padx=10, pady=10)

# Label 3
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# Label 4
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# Entry
entry = Entry(width=10)
print(entry.get())
entry.grid(column=1, row=0)

# keeps window on the screen and listens to the users
window.mainloop()
