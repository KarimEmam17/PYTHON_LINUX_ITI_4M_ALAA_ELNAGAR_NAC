from  tkinter import *


calculator= Tk()
calculator.title("calculator")

v = StringVar()
ENTRY_BOX=Entry(calculator,width=40,borderwidth=5,textvariable=v)
ENTRY_BOX.grid(row=0,column=0,columnspan=5,padx=40,pady=10)

def button_click(number):
  current=ENTRY_BOX.get()
  ENTRY_BOX.delete(0, END)
  ENTRY_BOX.insert(0, str(current)+str(number))
   
def fun_button_devision():
    first_number=ENTRY_BOX.get()
    global operation_selection
    operation_selection=3
    global f_num
    f_num=int(first_number)
    ENTRY_BOX.delete(0, END)
def fun_button_multiplay():
    first_number=ENTRY_BOX.get()
    global operation_selection
    operation_selection=2
    global f_num
    f_num=int(first_number)
    ENTRY_BOX.delete(0, END)
def fun_button_minus():
    first_number=ENTRY_BOX.get()
    global operation_selection
    operation_selection=1
    global f_num
    f_num=int(first_number)
    ENTRY_BOX.delete(0, END)

def fun_button_equal():
    global operation_selection
    second_num=ENTRY_BOX.get()
    ENTRY_BOX.delete(0, END)
    if operation_selection%4==0:
        ENTRY_BOX.insert(0, f_num+int(second_num))
    elif operation_selection%4==1:
        ENTRY_BOX.insert(0, f_num-int(second_num))
    elif operation_selection%4==2:
        ENTRY_BOX.insert(0, f_num*int(second_num))
    elif operation_selection%4==3:
        ENTRY_BOX.insert(0, float(f_num/int(second_num)))
def fun_button_plus():
    first_number=ENTRY_BOX.get()
    global operation_selection
    operation_selection=0
    global f_num
    f_num=int(first_number)
    ENTRY_BOX.delete(0, END)
def fun_button_new():
    global f_num
    f_num=0
    ENTRY_BOX.delete(0, END)
#defien buttons 
button_7=Button(calculator,text="7",command=lambda:button_click(7),padx=40,pady=20).grid(column=0,row=1)
button_8=Button(calculator,text="8",command=lambda:button_click(8),padx=40,pady=20).grid(row=1,column=1)
button_9=Button(calculator,text="9",command=lambda:button_click(9),padx=40,pady=20).grid(row=1,column=2)
button_devision=Button(calculator,text="/",command=fun_button_devision,padx=40,pady=20).grid(row=1,column=3)
button_4=Button(calculator,text="4",command=lambda:button_click(4),padx=40,pady=20).grid(row=2,column=0)
button_5=Button(calculator,text="5",command=lambda:button_click(5),padx=40,pady=20).grid(row=2,column=1)
button_6=Button(calculator,text="6",command=lambda:button_click(6),padx=40,pady=20).grid(row=2,column=2)
button_multiplay=Button(calculator,text="*",command=fun_button_multiplay,padx=40,pady=20).grid(row=2,column=3)
button_1=Button(calculator,text="1",command=lambda:button_click(1),padx=40,pady=20).grid(row=3,column=0)
button_2=Button(calculator,text="2",command=lambda:button_click(2),padx=40,pady=20).grid(row=3,column=1)
button_3=Button(calculator,text="3",command=lambda:button_click(3),padx=40,pady=20).grid(row=3,column=2)
button_minus=Button(calculator,text="-",command=fun_button_minus,padx=40,pady=20).grid(row=3,column=3)

button_new=Button(calculator,text="C",command=fun_button_new,padx=40,pady=20).grid(row=4,column=0)
button_0=Button(calculator,text="0",command=lambda:button_click(0),padx=40,pady=20).grid(row=4,column=1)
button_equal=Button(calculator,text="=",command=fun_button_equal,padx=40,pady=20).grid(row=4,column=2)
button_plus=Button(calculator,text="+",command=fun_button_plus,padx=40,pady=20).grid(row=4,column=3)

















calculator.mainloop()