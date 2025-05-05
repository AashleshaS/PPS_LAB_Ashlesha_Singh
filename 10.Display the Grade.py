m1=float(input("subject 1: "))
m2=float(input("subject 2: "))
m3=float(input("subject 3: "))
m4=float(input("subject 4: "))
m5=float(input("subject 5: "))

avg=(m1+m2+m3+m4+m5)/5.0
print(f"Average Marks: {avg:.2f}")

if avg>=90.00 and avg<=100.00:
	print("Grade: A")
elif avg>=80.00 and avg<=89.00:
	print("Grade: B")
elif avg>=70.00 and avg<=79.00:
	print("Grade: C")
elif avg>=60.00 and avg<=69.00:
	print("Grade: D")
else:
	print("Grade: F")