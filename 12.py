# 12) Write a program that generates a list of 20 random numbers between 1 and100.
#(a) Print the list.
#(b) Print the average of the elements in the list.
#(c) Print the largest and smallest values in the list.
#(d) Print the second largest and second smallest entries in the list
#(e) Print how many even numbers are in the list.


import random
l=[ ]
for i in range(20):
	ele=random.randint(1,100)
	print('ele',ele)
	l.append(ele)
print("element of list are",l)
average=sum(l)/len(l)
print("average is",average)
print("largest value is {} /n smallest value is{}".format(max(l),min(l)))
l.sort()
print("second largest element is",l[-2])
print("second smallest element is",l[1])
count=0
for i in l:
	if (i%2==0):
		count+=1
print("even number ",count)
