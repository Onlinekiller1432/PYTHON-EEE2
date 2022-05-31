# the programe to print the vowels in string
s1=input ("enter the string")
f=0
l1=['a','e','i','o','u']
for ch in s1:
	if (ch in l1):
		f=1
		break
if(f==1):
	print("the given string contains vowels")
else:
	print("the given string does not contains vowels")
