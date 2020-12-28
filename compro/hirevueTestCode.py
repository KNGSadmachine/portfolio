#input↓
#1000 1000 1000 1000 1000 1000
#Alice Alice Alice Alice Alice Alice

import sys

lines = []
for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))

Cal = list(map(str, lines[0].split()))
Name =  list(map(str, lines[1].split()))
#print(Cal)
#print(Name)

X = 0
for i in range(len(Name)):
    if Name[i] == 'Alice':
        X = X + int(Cal[i])

print(X)