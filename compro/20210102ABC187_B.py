N = int(input())
    
A = [list(map(int, input().split())) for k in range(N)]
X = 0
for i in range(N):
    for j in range(N):
    if i < j:
        if -1 <= (A[i][1]- A[j][1])/(A[i][0]- A[j][0]) <= 1:
        X += 1
print(X)