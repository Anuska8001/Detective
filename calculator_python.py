from tkinter import*
root = Tk()

def button_add(number):
    cur = t1.get()
    t1.delete(0,END)
    t1.insert(0,str(cur)+str(number))

def button_plus():
    first_num = t1.get()
    global f_num
    global opr
    opr = '+'
    f_num = int(first_num)
    t1.delete(0,END)

def button_minus():
    first_num = t1.get()
    global f_num
    global opr
    opr = '-'
    f_num = int(first_num)
    t1.delete(0,END)

def button_multiply():
    first_num = t1.get()
    global f_num
    global opr
    opr = '*'
    f_num = int(first_num)
    t1.delete(0,END)

def button_divide():
    first_num = t1.get()
    global f_num
    global opr
    opr = '/'
    f_num = int(first_num)
    t1.delete(0,END)

def button_delete():
    t1.delete(0,END)

def button_equal():
    sec_num = t1.get()
    t1.delete(0,END)
    
    global opr
    
    if opr == '+':
        t1.insert(0, f_num + int(sec_num))
    elif opr == '-':
        t1.insert(0, f_num - int(sec_num))
    elif opr == '*':
        t1.insert(0, f_num * int(sec_num))
    elif opr == '/':
        t1.insert(0, f_num / int(sec_num))

root.configure(background = "blue")
root.title('CALCULATOR')
root.resizable(0,0)

t1 = Entry(root, width = "35", borderwidth = "5", bg = 'yellow', fg = 'red', font = ('arial',15))
t1.grid(row = 0, column = 0, columnspan = 4, padx = 15, pady = 15)

btn1 = Button(root, text = '1', padx = 60, pady = 20, font = ('arial',15), command =  lambda:button_add(1))
btn2 = Button(root, text = '2', padx = 60, pady = 20, font = ('arial',15), command =  lambda:button_add(2))
btn3 = Button(root, text = '3', padx = 60, pady = 20, font = ('arial',15), command =  lambda:button_add(3))

btn4 = Button(root, text = '4', padx = 60, pady = 20, font = ('arial',15), command =  lambda:button_add(4))
btn5 = Button(root, text = '5', padx = 60, pady = 20, font = ('arial',15), command =  lambda:button_add(5))
btn6 = Button(root, text = '6', padx = 60, pady = 20, font = ('arial',15), command =  lambda:button_add(6))

btn7 = Button(root, text = '7', padx = 60, pady = 20, font = ('arial',15), command =  lambda:button_add(7))
btn8 = Button(root, text = '8', padx = 60, pady = 20, font = ('arial',15), command =  lambda:button_add(8))
btn9 = Button(root, text = '9', padx = 60, pady = 20, font = ('arial',15), command =  lambda:button_add(9))

btn0 = Button(root, text = '0', padx = 60, pady = 20, font = ('arial',15), command =  lambda:button_add(0))
btnplus = Button(root, text = '+', padx = 60, pady = 20, font = ('arial',15), command = button_plus)
btnequal = Button(root, text = '=', padx = 60, pady = 20, font = ('arial',15), command = button_equal)

btnminus = Button(root, text = '-', padx = 60, pady = 20, font = ('arial',15), command = button_minus)
btnmultiply = Button(root, text = '*', padx = 60, pady = 20, font = ('arial',15), command = button_multiply)
btndivide = Button(root, text = '/', padx = 60, pady = 20, font = ('arial',15), command = button_divide)

btnclear = Button(root, text = 'Clear', padx = 190, pady = 20, font = ('arial',15), command = button_delete)

btn9.grid(row = 2, column = 0)
btn8.grid(row = 2, column = 1)
btn7.grid(row = 2, column = 2)

btn6.grid(row = 3, column = 0)
btn5.grid(row = 3, column = 1)
btn4.grid(row = 3, column = 2)

btn3.grid(row = 4, column = 0)
btn2.grid(row = 4, column = 1)
btn1.grid(row = 4, column = 2)

btn0.grid(row = 5, column = 0)
btnplus.grid(row = 5, column = 1)
btnequal.grid(row = 5, column = 2)

btnminus.grid(row = 6, column = 0)
btnmultiply.grid(row = 6, column = 1)
btndivide.grid(row = 6, column = 2)

btnclear.grid(row = 7, column = 0, columnspan = 3)

root.mainloop()

