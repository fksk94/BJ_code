from collections import deque
import sys


def bfs(D):
    global max_cnt
    res = 1
    S = deque([D])
    visit[D] = False
    while S:
        tmp = S.popleft()
        if dic[tmp]:
            for i in dic[tmp]:
                if visit[i]:
                    S.append(i)
                    visit[i] = False
        res += 1
    if max_cnt < res:
        L.clear()
        L.append(D)
        max_cnt = res
    elif max_cnt == res:
        L.append(D)
    return


input = sys.stdin.readline

N, M = map(int, input().split())
L = []
max_cnt = 0
dic = [list() for i in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    dic[b].append(a)

for key in range(len(dic)):
    if dic[key]:
        visit = [True] * (N+1)
        bfs(key)

for i in L:
    print(i, end=' ')

