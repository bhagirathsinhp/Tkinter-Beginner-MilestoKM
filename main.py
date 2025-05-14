from tkinter import *

def button_clicked():
    # my_label.config(text='Button Got Clicked')
    # my_label.config(text=inputs.get())
    miles = inputs.get()
    km = int(miles) * 1.6
    rounded_km = round(km, 2)
    my_answer.config(text=rounded_km)

window = Tk()
window.title("GUI Program")
window.minsize(600, 600)
window.config(padx=100, pady=200)

my_label = Label(text="Miles", font=('Arial', 20, 'normal'))
# my_label['text'] = "Some Text"
# my_label.config(text="MY LABEL", padx=50, pady=50)
my_label.config(padx=20, pady=20)
my_label.grid(column=2, row=0)

my_label2 = Label(text='is equal to', font=('Arial', 20, 'normal'))
my_label2.grid(column=0, row=1)

my_answer = Label(text=0, font=('Arial', 20, 'normal'))
my_answer.config(padx=20, pady=20)
my_answer.grid(column=1, row=1)

my_label3 = Label(text="KM", font=('Arial', 20, 'normal'))
my_label3.grid(column=2, row=1)

#Button
button = Button(text='Click Me', command=button_clicked)
button.config(padx=20, pady=20)
button.grid(column=1, row=2)

# button2 = Button(text="New Button")
# button2.grid(column=2, row=0)

#Entry Component = Input
inputs = Entry(width=20)
inputs.insert(END, string="0")
inputs.grid(column=1, row=0)

window.mainloop()