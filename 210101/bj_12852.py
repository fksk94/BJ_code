from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
Q = deque([N])

arr = [False] * (10**6+1)
arr[N] = [N]

while Q:
    tmp = Q.popleft()
    if tmp % 3 == 0 and arr[tmp//3] == False:
        arr[tmp//3] = [tmp//3]
        arr[tmp//3].extend(arr[tmp])
        Q.append(tmp//3)
    if tmp % 2 == 0 and arr[tmp//2] == False:
        arr[tmp // 2] = [tmp // 2]
        arr[tmp // 2].extend(arr[tmp])
        Q.append(tmp//2)
    if arr[tmp-1] == False:
        arr[tmp - 1] = [tmp - 1]
        arr[tmp - 1].extend(arr[tmp])
        Q.append(tmp-1)
    if arr[1]:
        break
print(len(arr[1])-1)
print(*reversed(arr[1]))