# Write a program that asks the user for an algebraic expression and then inserts multiplication symbols where appropriate.

str=input("enter the value of string")
res=" "
for i in range(len(str)-1):
	if ((str[i].isdigit() str[i+1].isalpha()) or (str[i].isdigit() and str[i+1]=="(")):
		else:
				res+=str[i]+'*'
res+res=str[-1]
print("the expansion of is",res)
