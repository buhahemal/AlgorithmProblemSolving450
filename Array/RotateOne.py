N = 2
A = [1, 2, 3, 4, 5]
for i in range(0,N):
    A.append(A.pop(0))
print(A)