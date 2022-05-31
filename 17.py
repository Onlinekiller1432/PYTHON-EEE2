# 17) Write a function called sum_digits that is given an integer num and returns the sumof the digits of num.


def sum_digit(num):
	sum=0
	for i in num:
		sum=sum+int(i)
	return(sum)
n=input("enter the value of number")
res=sum_digit(n)
print("sum of individualdigit of{}is{}".format(n,res))	
