a, b, c = map(int, input())
A = [a,b,c]
X = 0
for i in range(len(A)):
  if A[i] == 1:
  	X = X + 1
  else:
    X = X

print(X)