import random
l=[]
for i in range(100):
	ele=random.randint(0,1)
	l.append(ele)
print(l)
c=0
m_count=0
for j in l:
	if(j==0):
		c+=1
else:
	if(c>m_count):
		m_count=c
	c=0
print("longest runs of zeros",m_count)
