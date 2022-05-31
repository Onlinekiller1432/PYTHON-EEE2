# TO CHECK THE GIVEN THE STRING IS SAME LENGTH OR NOT
s1=input ("enter the string of 1")
s2=input("enter the string of 2")
l1=len(s1)
l2=len(s2)
if (l1!=l2):
	 print("the given string {},{} is not in equql length".format(s1,s2))
else:
	for i in range(0,l1):
		print(s1[i],s2[i],end=" ")						
		
