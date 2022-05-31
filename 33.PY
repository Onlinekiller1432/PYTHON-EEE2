# 33) Write a program to demonstrate Try/except/else.

def divide(a,b):
	try:
		res=a/b
	except ZeroDivisionError:
		print("b value should  not be zero")
	else:
		print("result of division is",res)
	finally:
		print("program demonstrating exceptions")
a=int(input("enter first number"))
b=int(input("enter second number"))
divide(a,b)
