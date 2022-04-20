from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, p):
    q.append([x, y])
    temp = a[x][y]
    c[x][y] = p
    cnt, r = 1, 0
    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == temp and c[nx][ny] == 0:
                    c[nx][ny] = p
                    cnt += 1
                    q.append([nx, ny])
                elif a[nx][ny] == 0 and p not in c[nx][ny]:
                    c[nx][ny].append(p)
                    cnt += 1
                    r += 1
                    q.append([nx, ny])
    return cnt, r


def fall(x, y):
    flag = 0
    for i in range(x+1, n):
        nx = i
        if a[i][y] > -2:
            flag = 1
            break
    if flag:
        a[nx-1][y] = a[x][y]
    else:
        a[nx][y] = a[x][y]
    a[x][y] = -2


n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
while True:
    print(a)
    q = deque()
    c = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                c[i][j] = []

    p, b = 1, []
    for i in range(n):
        for j in range(n):
            if a[i][j] > 0 and c[i][j] == 0:
                cnt, r = bfs(i, j, p)
                if cnt > 1:
                    b.append([cnt, r, i, j, p])
                p += 1

    if not b:
        break

    b = sorted(b)

    cnt = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > 0 and c[i][j] == b[-1][-1]:
                a[i][j] = -2
                cnt += 1
            elif a[i][j] == 0 and b[-1][-1] in c[i][j]:
                a[i][j] = -2
                cnt += 1
    print('dawd',a)
    ans += cnt ** 2
    [print(cnt)]
    for i in range(n-2, -1, -1):
        for j in range(n):
            if a[i][j] >= 0 and a[i+1][j] == -2:
                fall(i, j)

    a = list(zip(*a))[::-1]
    a = [list(s) for s in a]
    
    for i in range(n-2, -1, -1):
        for j in range(n):
            if a[i][j] >= 0 and a[i+1][j] == -2:
                fall(i, j)

print(ans)