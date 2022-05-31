l=[1,2,5,6,7,8,9,7,8,2,5,4,6,22,54,45,54,6,8,7,9,54,]
res=[ ]
for i in l:
	if i not in res:
		res.append(i)
print("list after remaining reapeated element is",res)
