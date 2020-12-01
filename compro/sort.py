#def solution(A):
A = [1,2,3,4]
A = [int(x) for x in list(str(A))]

if len(A)%2 == 0:
    Half_A = A[:len(A)//2]
    Flah_A = sorted(A[len(A)//2:], reverse=True)
    Memory_0 = list(range(0))
    for i in range(len(A)//2):
        Memory_0.append(Half_A[i])
        Memory_0.append(Flah_A[i])
    Output = 0
    for j in range(len(Memory_0)-1,-1,-1):
        Output = Output + Memory_0[len(Memory_0)-(j+1)]*10**j
    print(Output)