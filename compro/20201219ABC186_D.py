import itertools
N = int(input())
A = list(map(int,input().split()))
X = 0
    
All = itertools.combinations(A, 2)
DB = list(range(0))
for i in All:
    DB.append(i)
for i in range(len(DB)):
    X += abs(DB[i][0] - DB[i][1])
print(X)