#5) Use a for loop to print a triangle like the one below. Allow the user to specify how high the triangle should be.
#*
#**
#***
#**** 
n=int(input("enter the value"))
for i in range(n+1):
    for j in range(i+1):
        print('*',end=' ')
    print()
