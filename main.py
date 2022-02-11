from tkinter import *
root = Tk()
e = Entry(root,width=38, borderwidth=2)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_press(num):
    display = e.get()
    e.delete(0,END)
    e.insert(0,str(display)+str(num))

def button_clear():
    e.delete(0, END)

def button_sum():
    first_number = e.get()
    global f_number
    f_number = int(first_number)
    global operation
    operation = "add"
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global f_number
    f_number = int(first_number)
    global operation
    operation = "sub"
    e.delete(0,END)

def button_mult():
    first_number = e.get()
    global f_number
    f_number = int(first_number)
    global operation
    operation = "mult"
    e.delete(0,END)

def button_div():
    first_number = e.get()
    global f_number
    f_number = int(first_number)
    global operation
    operation = "div"
    e.delete(0,END)

def button_eql():
    second_number = e.get()
    e.delete(0,END)
    if(operation == "add"):
        e.insert(0,f_number + int(second_number))
    elif (operation == "sub"):
        e.insert(0, f_number - int(second_number))
    elif (operation == "mult"):
        e.insert(0, f_number * int(second_number))
    elif (operation == "div"):
        e.insert(0, f_number / int(second_number))
#define

button1 = Button(root, text="1", padx=40,pady=20, command=lambda : button_press(1))
button2 = Button(root, text="2", padx=40,pady=20, command=lambda : button_press(2))
button3 = Button(root, text="3", padx=40,pady=20, command=lambda : button_press(3))
button4 = Button(root, text="4", padx=40,pady=20, command=lambda : button_press(4))
button5 = Button(root, text="5", padx=40,pady=20, command=lambda : button_press(5))
button6 = Button(root, text="6", padx=40,pady=20, command=lambda : button_press(6))
button7 = Button(root, text="7", padx=40,pady=20, command=lambda : button_press(7))
button8 = Button(root, text="8", padx=40,pady=20, command=lambda : button_press(8))
button9 = Button(root, text="9", padx=40,pady=20, command=lambda : button_press(9))
button0 = Button(root, text="0", padx=40,pady=20, command=lambda : button_press(0))
button_add = Button(root, text="+", padx=40,pady=20, command=button_sum)
button_sub = Button(root, text="-", padx=40,pady=20, command=button_sub)
button_mult = Button(root, text="*", padx=40,pady=20, command=button_mult)
button_div = Button(root, text="/", padx=40,pady=20, command=button_div)
button_clr = Button(root, text="clr", padx=40,pady=20, command=button_clear)
button_equal = Button(root, text="=", padx=40,pady=20, command=button_eql)

#Display
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button_mult.grid(row=3,column=3)

button0.grid(row=4,column=0)
button_div.grid(row=4,column=1)
button_clr.grid(row=4,column=2)
button_equal.grid(row=4,column=3)

#loop for run
root.mainloop()