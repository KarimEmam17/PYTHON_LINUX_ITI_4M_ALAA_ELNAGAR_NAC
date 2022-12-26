import sys,time,os,colorama
os.system("") 
from time import sleep

start=1
m=0
def pos (x,y) : #{
	return '\x1b[' + str(y) +';'+ str(x) + 'H';

# print(pos(30,10)+"9")
# time.sleep(3)	
# print(pos(50,10)+"9")
while start:
	sys.stdout.write("\033[2J")
	for n in range(1,10,1):
		for s in range(1,n,1):
			print(pos((20+(s*2)),(10+n)) +"*",end=" ")
			
	for n in range(1,10,1):
		for s in range((n+1),10,):
			print(pos((40-(s*2)),(19+n)) +"*",end=" ")	
	m=int(input(pos(1,1)+ "\n  continue= 1"))		
	sys.stdout.write("\033[2J")	
	
	for n in range(1,10,1):
		for s in range(1,n,1):
			print(pos((36+(s*2)),(18+n)) +"*",end=" ")
	for n in range(1,10,1):
		for s in range(1,n,1):
			print(pos((38-(s*2)),(18+n)) +"*",end=" ")
	m=int(input(pos(1,1)+ "\n do  u want  to  end? end=0, continue= 1"))				
	sys.stdout.write("\033[2J")
	for n in range(1,10,1):
		for s in range(1,n,1):
			print(pos((36+(n*2)),(19+s)) +"*",end=" ")
	for n in range(1,10,1):
		for s in range(1,n,1):
			print(pos((36+(n*2)),(20-s)) +"*",end=" ")
	m=int(input(pos(1,1)+ "\n do  u want  to  end? end=0, continue= 1"))				
	sys.stdout.write("\033[2J")	
	for n in range(1,10,1):
		for s in range(1,n,1):
			print(pos((36+(s*2)),(21-n)) +"*",end=" ")
	for n in range(1,10,1):
		for s in range(1,n,1):
			print(pos((38-(s*2)),(21-n)) +"*",end=" ")			
	m=int(input(pos(1,1)+ "\n do  u want  to  end? end=0, continue= 1"))			
	sys.stdout.write("\033[2J")				
	
	# start=int(input(pos(1,1)+ "\n do  u want  to  end? end=0, continue= 1"))
	sys.stdout.write("\033[2J")