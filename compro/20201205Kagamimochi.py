N = int(input())
A = list(range(0))
for _ in range(N):
  A.append(int(input()))

A = sorted(A)
X = 0

for i in range(len(A) -(2-N%2)):
  if A[i] == A[i+1]:
    A[i+1] = 0
    A = sorted(A)
for i in range(len(A) -(2-N%2)):
  if A[i] == 0:
    X += 1
    
print(X)
print(N - (X))
