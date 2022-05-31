#Write a function called merge that takes two already sorted lists of possibly different lengths, and merges them into a single sorted list. (a) Do this using the sort method. (b) Do this without using the sort method.


def merge (l1,l2):
    l=l1+l2
    for i in range(0,len(l)-1):
        for j in range(0,i):
            if(l[i]>[j]):
                l[i],l[j]==l[j],l[i]
    print("sorted list is :",l)
l1=[2,25,8,9,6,]
l2=[9,7,5,9,6,8,]
res=(l1+l2)
res.sort()
print(res)
