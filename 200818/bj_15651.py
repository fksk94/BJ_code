import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

arr = [1, 2, 3, 4, 5, 6, 7, 8]
result = []

def backTracking(cir_count) :
    global M, N

    if M == cir_count :
        result.append(arr[0:M])
        return

    for i in range(1, N+1) :
        arr[cir_count] = i
        backTracking(cir_count+1)

backTracking(0)

for i in result :
    for j in i :
        print(j, end=' ')
    print()