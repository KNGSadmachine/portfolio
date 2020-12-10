N, A, B = map(int,input().split())

X = 0  
for i in range(N+1):
  if i <= 9:
    if A <= i <= B:
      X = X + i
  else:
    I = i
    i = [int(x) for x in list(str(i))]
    if A <= sum(i) <= B:
      X = X + I      
    else:
      X = X

print(X)