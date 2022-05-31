# 13) Write a program that asks the user for an integer and creates a list that consists of the factors of that integer.


num=int(input("enter the vlue of number"))
l=[]
for i in range(1,num+1):
	if (num%i==0):
		l.append(i)
print("the factors of {} is{} ".format(num,l))
