A, B, C = map(int,input().split())
Val = B**C%4

A = str(A)

if A[-1] == "2":
  Two = [6,2,4,8]
  print(Two[Val])
  
elif A[-1] == "3":
  Three = [1,3,9,7]
  print(Three[Val])

elif A[-1] == "4":
  For = [6,4,6,4]
  print(For[Val])

elif A[-1] == "7":
  Seven = [1,7,9,3]
  print(Seven[Val])

elif A[-1] == "8":
  Eight = [6,8,4,2]
  print(Eight[Val])

elif A[-1] == "9":
  Nine = [1,9,1,9]
  print(Nine[Val])
  
else:
  print(A[-1])