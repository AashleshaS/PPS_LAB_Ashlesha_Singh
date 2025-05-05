a=int(input("digit1 (0-9): "))
b=int(input("digit2 (0-9): "))
c=int(input("digit3 (0-9): "))
if(0<=a<10) and (0<=b<10) and (0<=c<10):
	d=[]
	d.append(a)
	d.append(b)
	d.append(c)
	for i in range(0,3):
		for j in range(0,3):
			for k in range(0,3):
				if(i!=j & j!=k & k!=i):
					print(d[i],d[j],d[k],sep='')
else:
	print("Invalid")