N = int(input())
A = list(map(int, input().split()))

ans = float('inf')
for i in A:
    ans = min(ans, len(bin(i)) - bin(i).rfind("1") -1 )

print(ans)