    Battery, Caf, T = map(int,input().split())
    AB = [map(int, input().split()) for _ in range(Caf)]
    A, B = [list(i) for i in zip(*AB)]
     
    for i in range(len(A)):
      A.append(B[i])
    A.insert(0,0)
    A.append(T)
    A = sorted(A)
     
    Box = list(range(0))
    for i in range(len(A)-1):
      X = A[i+1] - A[i]
      Box.append(X)
    E = 0
    for i in range(len(Box)):
      if i%2 == 0:
        Box[i] = -1*Box[i]
     
    #print(Box)
    Y = 0
    for i in Box:
      if Battery + i <= 0:
        #print(Battery +i)
        Y += 1
        
    if Y >= 1:
      print("No")
    else:
      Ans = Battery + sum(Box)
      if Ans > 0:
        print("Yes")
      else:
        print("No")