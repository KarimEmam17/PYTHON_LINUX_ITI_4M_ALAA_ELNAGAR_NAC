import os
from time import sleep
start=1
while  start:
	mode=int(input("select mode  from  one  mode Seintific (1) , programming (2)"))
	if mode == 1:
		first_num=int(input("Enter the first NUM "))
		second_num=int(input("Enter the second NUM "))
		oper=int(input("Select operation add (1) , sub (2) , div (3), mul(4) , mod (5), exp (6) "))
		if oper== 1:
			result=first_num + second_num
			print(result)
		elif oper == 2:	
			result=first_num - second_num
			print(result)
		elif oper == 3:
			result=first_num / second_num
			print(result)
		elif oper == 4:
			result=first_num * second_num
			print(result)
		elif oper == 5:
			result=first_num % second_num
			print(result)
		elif oper == 6:
			result=first_num ** second_num
			print(result)
	elif mode == 2:
		first_num=int(input("Enter the first NUM "))
		#second_num=input("Enter the second NUM")
		oper=int(input("Select operation bin(1),hex(2),dec(3),oct(4)"))
		if oper== 1:
			result=bin(first_num) 
			print(result)
		elif oper== 2:	
			result=hex(first_num) 
			print(result)
		elif oper== 3:
			result=dec(first_num) 
			print(result)
		elif oper== 4:
			result=oct(first_num) 
			print(result)
	start=int(input("do  you  want to end  ? end=0 continue=1 "))
	sleep(10)
	
	os.system('cls')
		