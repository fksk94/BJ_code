from sys import stdin
input = stdin.readline

n, x, y = map(int, input().split())
res = 0

def div_2(x):
    if x == 1:
        return 0
    return div_2(x//2) + 1

arr = [2, 6, 2, 22, 2, 6, 2, 86]

for i in range(3, n):
    arr.extend(arr[:])
    arr[-1] += 4**i

while y:
    tmp = div_2(y)
    res += 4 ** tmp
    y -= 2 ** tmp

for i in range(x):
    res += arr[i]

print(res)