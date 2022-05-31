# 19) Write a function called number_of_factors that takes an integer and returns howmany factors the number has.


def  number_of_factor(num):
	count=0
	for i in range(1,num+1):
		if(num%i==0):
			count=+1
	return(count)
n=int(input("enter the number"))
resultr_of_factor
print("factors of{}is{}.format (num,count))
