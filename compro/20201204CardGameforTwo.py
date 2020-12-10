N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse = True)

Alice = list(range(0))
Bob = list(range(0))

if len(A)%2 == 0:
  for i in range(N-len(A)//2):
    Alice.append(A[2*i])
    Bob.append(A[2*i +1])
else:
  for i in range(N-len(A)//2-1):
    Alice.append(A[2*i])
    Bob.append(A[2*i +1])
  Alice.append(A[len(A) -1])

print(sum(Alice) - sum(Bob))