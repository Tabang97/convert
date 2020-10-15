from tkinter import *

Roses = Tk()
Roses.title("Temperature Convertor")
Roses.geometry("800x400")
Roses.configure(background="orange")


def convert():
    if txt_box1:
        celcius = int(float(celTempVar.get()))
        fahreinheit = celcius * (9 / 5) + 32
        txt_box3.configure(text=fahreinheit)


def celtofar():
    if txt_box2:
        fahreinheit = int(float(fahTempVar.get()))
        celcius = (fahreinheit - 32) * (5 / 9)
        txt_box3.configure(text=celcius)


def clear_function():
    txt_box1.delete(0, END)
    txt_box2.delete(0, END)
    txt_box3.configure(text="")


def quit():
    Roses.destroy()


def Cel_activation():
    txt_box1.configure(state="normal")
    txt_box2.configure(state="disable")


def Fah_activation():
    txt_box2.configure(state="normal")
    txt_box1.configure(state="disable")


celTempVar = IntVar()
fahTempVar = IntVar()

# 1st label
label = LabelFrame(Roses, text="Celcius to Fahrenheit", padx=20, pady=20, bg="purple")
label.grid(row=0, column=0)
txt_box1 = Entry(label, width="30")
txt_box1.grid(row=1, column=0)

# 2nd label
label2 = LabelFrame(Roses, text="Fahrenheit to Celsius", padx=20, pady=20, bg="purple")
label2.grid(row=0, column=2)
txt_box2 = Entry(label2, width="30")
txt_box2.grid(row=1, column=2)

# 3rd label
label3 = Label(Roses, text="RESULT", bg="sky blue")
label3.grid(row=9, column=0)
txt_box3 = Label(Roses, width="30", bg="grey", text="")
txt_box3.grid(row=9, column=1)

# convertor button
button1 = Button(Roses, text="Convert", bg="yellow", command=convert)
button1.grid(row=8, column=0)

button1 = Button(Roses, text="Convert", bg="yellow", command=convert)
button1.grid(row=7, column=0)
# clear button
button2 = Button(Roses, text="Clear", bg="navy", command=clear_function)
button2.grid(row=8, column=2)

# exit button
button3 = Button(Roses, text="Exit Program", bg="red", command=quit)
button3.grid(row=9, column=2)

# C_to_F_Activation_button
button3 = Button(Roses, text="Activate Celsius/Fahrenheit", bg="green", command="Cel_activation")
button3.grid(row=3, column=0)

# F_to_A_Activation_button
button4 = Button(Roses, text="Activate Fahrenheit/Celsius", bg="green", command="Fah_activation")
button4.grid(row=3, column=2)
Roses.mainloop()
