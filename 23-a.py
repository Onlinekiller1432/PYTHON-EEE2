def merge(list1,list2):
    l=list1+list2
    l.sort()
    print("sorted list is",l)
l=input("enter elements saparated by ,").split(",")
l1=[]
for i in l:
    l1.append(int(i))
l=input("enter elements saparated by ,").split(",")
l2=[]
for i in l:
    l2.append(int(i))
merge(l1,l2)
