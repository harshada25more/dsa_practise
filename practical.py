def avg(l):
      average=sum(l)/len(l)
      print(average)
	
	
def high(l):
	max=0
	for i in range(len(l)):
		if (max<l[i]):
			max=l[i]
	print("HIGHEST BOOKS BORROWED BY STUDENTS IS=",max)

def low(l):
	min=0
	for i in range(len(l)):
		if (min>l[i]):
			min=l[i]
	print("LOWEST BOOKS BORROWED BY STUDENTS IS=",min)
	
def count(l):
	cnt=0
	for i in range(len(l)):
		if l[i]==0:
			cnt=cnt+1
		
	print("ZERO BOOKS BORROWED BY STUDENT",cnt)
	
def frequency(l):
       freq=max(set(l),key=l.count)
       print(freq)
	 
	



lib=[]
n=int(input("ENTER THE TOTAL NUMBER OF STUDENTS=")) 
print("\n")
#accepting total num of books borrowed by students
for i in range(n):
	a=int(input("TOTAL NUMBER OF BOOKS BORROWED BY STUDENT="))
	lib.append(a)
	
print(lib)
	
#display menu

while True:
	print("###LIBRARY RECORD###")
	print("1.AVG")
	print("2.HIGHEST")
	print("3.LOWEST")
	print("4.COUNT")
	print("5.FREQUENCY")
	print("6.EXIT")
	
#accepting choice by user
	ch=int(input("ENTER YOUR CHOICE:"))
	
	if (ch==1):
		avg(lib)
	elif (ch==2):
		high(lib)
	elif (ch==3):
		low(lib)
	elif (ch==4):
		count(lib)
	elif (ch==5):
		frequency(lib)
	elif (ch==6):
		print("THANK YOU")
		exit()
	else:
		print("INVALID CHOICE")

