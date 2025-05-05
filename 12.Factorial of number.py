def fact(n):
	f=1
	while(n!=0):
		f=f*n
		n=n-1
	return f

n=int(input("Enter a number : "))
if n>=0:
	f=fact(n)
	print("Factorial of given number is :",f)
else:
	print("Enter a positive number")