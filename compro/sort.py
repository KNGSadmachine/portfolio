#Question
#There is a company that has a way creative way of managing its accounts. 
#Every time they want to write down a number, they shuffle its digits in thw following way :
#they alternatibvely write one digit from the front of the number and one digit from the back, 
#then the second digit from the front and the second form the back,
#and son in until the length of the shuffled number is the same as that of the original.
#
#Write a function
#   def solution(A)
#that, givin a positive integer A, returns its shuffled representation.
#For example, given A = 123456 the function should return 162534.
#Given A = 130 the function should return 103.
#Assume that:
#   A is an interger within the range [0..100,000,000].
#In your solution, focus on correctness.
#The performance of your solution will not be the foucus of the assessment.

#ANSWER
#def solution(A):
A = input("Plz input number : ")
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
    #return(Output)

else:
    Half_A = A[:len(A)//2+1]
    Flah_A = sorted(A[len(A)//2+1:], reverse=True)
    Memory_0 = list(range(0))
    for i in range(len(A)//2):
        Memory_0.append(Half_A[i])
        Memory_0.append(Flah_A[i])
    Memory_0.append(Half_A[-1])
    Output = 0
    for j in range(len(Memory_0)-1,-1,-1):
        Output = Output + Memory_0[len(Memory_0)-(j+1)]*10**j
    print(Output)
    #return(Output)
