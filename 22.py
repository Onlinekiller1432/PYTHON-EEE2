#22) Write a function called primes that is given a number n and returns a list of the first n primes. Let the default value of n be100.


def check_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return(False)
        else:
            return(True)
def prime(num=100):
    n=3
    l=[2]
    c=1
    while(c<num):
        if (check_prime(n)):
            l.append(n)
            c+=1
        n+=1
    return(l)
n=int(input("enter the value: "))
print(prime(n))
print('\n',prime())
