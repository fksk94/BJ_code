from sys import stdin
input = stdin.readline

N = int(input())
arr = [0] + [int(input()) for i in range(N)]
dp1 = [0] * (N+1)
dp2 = [0] * (N+1)
dp1[1], dp2[1] = arr[1], arr[1]
for i in range(2, len(arr)):
    dp2[i] = max(dp1[i-2], dp2[i-2], dp1[i-3], dp2[i-3]) + arr[i]
    dp1[i] = max(dp2[i-1], dp1[i-2], dp2[i-2]) + arr[i]

print(max(max(dp2), max(dp1)))