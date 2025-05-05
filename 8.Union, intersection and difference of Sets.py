a = list(map(int,input("Set A: ").split()))
A = set(a)
b = list(map(int,input("Set B: ").split()))
B = set(b)

# Write your code here to perform different operations
print("Union: ",A.union(B))
print("Intersection: ",A.intersection(B))
print("Difference: ",A.difference(B))