# Calculator-with-tkinter
Simple designed Calculator with tkinter, Responsive Calculator
from tkinter import *

win = Tk() 
win.title("Calculator!")
win.geometry("600x400")

def addition():
  num1 = e1.get()
  num2 = e2.get()
  answer = int(num1) + int(num2)
  result.configure(text= f"{num1} + {num2} = {answer}")



def subtraction():
  num1 = e1.get()
  num2 = e2.get()
  answer = int(num1) - int(num2)
  result.configure(text= f"{num1} - {num2} = {answer}")

def multiplication():
  num1 = e1.get()
  num2 = e2.get()
  answer = int(num1) * int(num2)
  result.configure(text= f"{num1} * {num2} = {answer}")


def Division():
  num1 = e1.get()
  num2 = e2.get()
  answer = int(num1) / int(num2)
  result.configure(text= f"{num1} ÷ {num2} = {answer}")

    



name = Label(win, text = 'Calculator App', font=('tohama', 24, 'bold'),fg='Black',bg='white')
name.place(x=190,y=0)

l1 = Label(win, text="Enter First Number:",  font=('tohama', 10, 'bold'),fg='Black',bg='white')
l2 = Label(win, text="Enter Second Number:",  font=('tohama', 10, 'bold'),fg='Black',bg='white')
e1 = Entry(win)
e2 = Entry(win)

l1.place(x= 50, y = 100)
e1.place(x= 200, y= 100)

l2.place(x= 50, y=150)
e2.place(x= 200, y=150 )

addb = Button(win, text = "ADD +", command = addition, font=('tohama', 10, 'bold'),fg='Black',bg='white')
subb = Button(win, text= "Subtract -", command = subtraction,  font=('tohama', 10, 'bold'),fg='Black',bg='white')
mullti = Button(win, text = "Multiply *", command = multiplication,  font=('tohama', 10, 'bold'),fg='Black',bg='white' )
divii = Button(win, text = "Divide ÷", command = Division,  font=('tohama', 10, 'bold'),fg='Black',bg='white' )

addb.place(x= 50, y=200)
subb.place(x= 150, y=200)
mullti.place(x= 150, y= 240)
divii.place(x= 250, y=200)

result = Label(win, text="Your Answer Appear Here!",  font=('tohama', 10, 'bold'),fg='Black',bg='white')
result.place(x=50, y = 300)




win.mainloop()
