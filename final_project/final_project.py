from tkinter import *


def timer_var():
	timer_var.var0=0
	timer_var.var1=0
	timer_var.var2=0

timer_var.var0=0
timer_var.var1=0
timer_var.var2= 0


timer_function_generator =Tk()
timer_function_generator.title("Interrupt Function Generator")

	
def Timer0_button():
	timer_var.var0=timer_var.var0+1
	if   timer_var.var0%2==0:
		timer0_button   =Button(timer_function_generator,text="interrupt0",padx=50,pady=50, command=timer_function_generator.destroy,bg='red').grid(row=3,column=2)
	elif timer_var.var0%2==1:
		timer0_button   =Button(timer_function_generator,text="interrupt0",padx=50,pady=50, command=Timer0_button,bg='green').grid(row=3,column=2)
		timer0_The_low_level_button=Button(timer_function_generator,text="The low level interrupt",padx=25,pady=25).grid(row=3,column=3)
		timer0_Any_logical_change_button=Button(timer_function_generator,text="Any logical change interrupt",padx=25,pady=25).grid(row=3,column=4)
		timer0_The_falling_edge_button=Button(timer_function_generator,text="The falling edge interrupt",padx=25,pady=25).grid(row=3,column=5)
		timer0_The_rising_edge_button=Button(timer_function_generator,text="The rising edge interrupt",padx=25,pady=25).grid(row=3,column=6)

def Timer1_button():
	timer_var.var1 +=1
	if   timer_var.var1%2==0:
		timer1_button   =Button(timer_function_generator,text="interrupt1",padx=50,pady=50,command=Timer1_button,bg='red').grid(row=6,column=2)
	elif timer_var.var1%2==1:
		timer1_button   =Button(timer_function_generator,text="interrupt1",padx=50,pady=50,command=Timer1_button,bg='green').grid(row=6,column=2)
	timer1_The_low_level_button=Button(timer_function_generator,text="The low level interrupt",padx=25,pady=25).grid(row=6,column=3)
	timer1_Any_logical_change_button=Button(timer_function_generator,text="Any logical change interrupt",padx=25,pady=25).grid(row=6,column=4)
	timer1_The_falling_edge_button=Button(timer_function_generator,text="The falling edge interrupt",padx=25,pady=25).grid(row=6,column=5)
	timer1_The_rising_edge_button=Button(timer_function_generator,text="The rising edge interrupt",padx=25,pady=25).grid(row=6,column=6)

def Timer2_button():
	timer_var.var2 +=1
	if timer_var.var2%2==0:
		timer2_button   =Button(timer_function_generator,text="interrupt2",padx=50,pady=50,command=Timer2_button,bg='red').grid(row=9,column=2)			
	elif timer_var.var2%2==1:
			timer2_button   =Button(timer_function_generator,text="interrupt2",padx=50,pady=50,command=Timer2_button,bg='green').grid(row=9,column=2)
			Timer2_button.timer2_The_falling_edge_button=Button(timer_function_generator,text="The falling edge interrupt",padx=25,pady=25).grid(row=9,column=5)
			Timer2_button.timer2_The_rising_edge_button=Button(timer_function_generator,text="The rising edge interrupt",padx=25,pady=25).grid(row=9,column=6)


		
		
top_label=Label(timer_function_generator,text="welcome to interrupt function generator").grid(row=0,column=5)
timer0_label= Label(timer_function_generator,text="interrupt0 button       ").grid(row=3,column=1)
if   timer_var.var0%2==0:
	timer0_button   =Button(timer_function_generator,text="interrupt0",padx=50,pady=50, command=Timer0_button,bg='red').grid(row=3,column=2)
elif timer_var.var0%2==1:
	timer0_button   =Button(timer_function_generator,text="interrupt0",padx=50,pady=50, command=Timer0_button,bg='green').grid(row=3,column=2)
timer1_label= Label(timer_function_generator,text="interrupt1 button       ").grid(row=6,column=1)
if   timer_var.var1%2==0:
	timer1_button=Button(timer_function_generator,text="interrupt1",padx=50,pady=50,command=Timer1_button,bg='red').grid(row=6,column=2)
elif timer_var.var1%2==1:
	timer1_button=Button(timer_function_generator,text="interrupt1",padx=50,pady=50,command=Timer1_button,bg='green').grid(row=6,column=2)
timer2_label= Label(timer_function_generator,text="interrupt2 button       ").grid(row=9,column=1)
if timer_var.var2%2==0:
	timer2_button=Button(timer_function_generator,text="interrupt2",padx=50,pady=50,command=Timer2_button,bg='red').grid(row=9,column=2)
elif timer_var.var2%2==1:
	timer2_button=Button(timer_function_generator,text="interrupt2",padx=50,pady=50,command=Timer2_button,bg='green').grid(row=9,column=2)








	timer_function_generator.mainloop()
