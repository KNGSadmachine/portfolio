N, X = map(int, input().split())
S = input()
for s in S:
    if s == 'o':
        X = X + 1
    else:
        if X == 0:
            X = X
        elif X >= 1:
            X = X - 1
             
print(X)