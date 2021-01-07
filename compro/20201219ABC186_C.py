N = int(input())
Ten = list(range(0))
Ans_x = list(range(0))
Ans_e = list(range(0))

for i in range(1,N+1,1):
  Ten.append(i)
Xen = [str(i) for i in Ten]
for i in range(len(Xen)):
  if "7" in Xen[i]:
    Ans_x.append(int(Xen[i]))

E = [oct(i) for i in Ten]
for i in range(len(E)):
  if "7" in E[i]:
    Ans_x.append(int(E[i],8))

print(N - len(list(set(Ans_x))))
