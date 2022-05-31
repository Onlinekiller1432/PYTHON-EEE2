#Write a class called Product.
#The class should have fields called name, amount, and holding the product’s name,
#the number of items of that product in stock, and the regular price of the product


class product:
    name=' '
    qty=0
    price=0.0
    def __init__(self,n,q,p):
        self.name=n
        self.qty=q
        self.price=p
    
    def get_price(self,no):
        disc=0
        cost=0
        if(no<10):
            disc=0
        elif(no>=10 and no<100):
            disc=10
        else:
            disc=20
        cost=no*self.price*((100-disc)/100)
        return(cost)

    def make_purchase(self,no):
        if(self.qty>no):
            self.qty-=no
            print("avilable qty after purchase is:",self.qty)
        else:
            print("out of stock")

p1=product("moto",500,10000)
print(p1.get_price(5))
print(p1.get_price(10))
print(p1.get_price(100))
(p1.make_purchase(100))
