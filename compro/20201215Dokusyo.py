# Buy 3
# Buy 2
# Buy 1
# read
# read

# [3,2,1,3,2]


import sys

lines = []
a = 0
b = 0
for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
#print(lines)
A = lines[0]
N, K = A.split()
N = int(N)
K = int(K)
#print(N,K)
Day = list(range(0))
for i in range(1,len(lines),1):
    Day.append(lines[i].split())

    
Ans = list(range(0))
Buy = list(range(0))

for i in range(len(Day)-1):
    if 'buy' in Day[i] :
        Ans.append(Day[i][1])
        print(Day[i][1])
    else:
        print(Day[i-(N-K)][1])