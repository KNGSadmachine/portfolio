N = int(input())
    
S = [input() for i in range(N)]
    
Ans = list(range(0))
    
for s in S:
    if ("!" + s) in S:
    Ans.append(s)
    break
        
if Ans == []:
    print("satisfiable")
else:
    print(Ans[0].lstrip("!"))