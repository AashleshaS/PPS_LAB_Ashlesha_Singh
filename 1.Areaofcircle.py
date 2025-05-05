r=float(input('Enter the radius : '))
if r>=0 and r<=100:
	a=float(3.14*r*r)
	print(f'Area of circle = {a:.6f}')
else:
	print('Enter a positive value upto 100\n')