#!/usr/bin/env python3
import sys
print("Program to tell if a number is Prime or not")
while True:
	try:
		a=int(input("Enter the number: "))
	except ValueError:
		print("Input must be integer. Don't Panic! Try Again :p ")
		continue		
	for i in range(2,int(a/2)):
		if(a%i==0):
			print(a," is NOT a prime number.It's divisible by ",i)
			break
		else:
			print(a," seems to be a prime number.... its NOT divisible by ",i)
	b=str(input('Do it again (y/n) : '))
	if(b=='y'or b=='Y'):
		continue
	else:
		sys.exit()

