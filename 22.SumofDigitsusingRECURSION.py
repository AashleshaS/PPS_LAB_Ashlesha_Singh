def Sumof(n):
	if n<10:
		return n
	return(n%10 + Sumof(n//10))

n=int(input())
print(Sumof(n))