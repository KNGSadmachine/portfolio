H, W = map(int, input().split())
A = [list(map(int, input().split())) for k in range(H)]
X = 0
Min = list(range(0))
DB = list(range(0))

for i in range(H):
  Min.append(min(A[i]))

Min_num = min(Min)
for i in range(H):
  for j in range(W):
    Num = A[i][j] - Min_num
    if Num > 0:
      DB.append(Num)
print(sum(DB))
