# (21) Write a function called root that is given a number x and an integer n and returns x1/n. In the function definition, set the default value of n to2.

def root(x,n=2):
    return(x**(1/n))
num=int(input("enter  "))
power=int(input("enter  "))
res=root(num,power)
print("{} power of 1/{} is : {}".format(num,power,res))
res2=root(num)
print("{} power of 1/2 is : {} ".format(num,res2))
