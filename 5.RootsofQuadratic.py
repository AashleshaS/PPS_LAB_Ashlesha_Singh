import math 

a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))

d=b**2-4*a*c

if d>=0:
	r1=(-b + math.sqrt(d))/(2*a)
	r2=(-b-math.sqrt(d))/(2*a)

	if d==0:
		print("The root is: {:.2f}".format(r1))
	else:
		print("The roots are: {:.2f} and {:.2f}".format(r1,r2))

else:
	rp=-b/(2*a)
	ip=math.sqrt(abs(d))/(2*a)
	print("The roots are: {:.2f}+{:.2f}j and {:.2f}-{:.2f}j".format(rp,ip,rp,ip))