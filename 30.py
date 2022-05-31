# 30) Write a Python class to implement pow(x,n).
class pow:
    x=0
    n=0
    def __init__(self,x1,n1):
        self.x=x1
        self.n=n1
        pow=abs(self.n)
        res=1
        for i in range(pow):
            res*=self.x
        if (self.n<0):
            print("power of ({},{}) is {}".format(x1,n1,1/res))
        else:
            print("power of ({},{}) is {}".format(x1,n1,res))
pow(2,3)
pow(2,-3)
