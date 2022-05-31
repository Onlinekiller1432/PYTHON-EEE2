#31) Write a Python class to reverse a string word by word.
class reverse:
    str=' '
    def __init__(self,s):
        self.str=s
    def rstr(self):
        l=self.str.split(' ')
        return(' '.join(reversed(l)))
s1=input("enter the string: ")
res=reverse(s1)
print("reversed string is word by word is",res.rstr())
