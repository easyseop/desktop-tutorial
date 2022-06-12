from calendar import c
from collections import deque 
from heapq import heappop,heappush
# grid= ["..FF","###F","###."]
# k = 4
grid = [".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.", ".#...####F", "...#......"]
k=6



arr = [list(i) for i in grid]
n = len(grid)
m = len(arr[0])



dx = [1,-1,0,0]
dy = [0,0,1,-1]

# d = deque()
h = [[0,0,0,0]] # cnt,k,x,y

z = 0


for i in range(n):
    for j in range(m):
        if arr[i][j] == '.':
            z+=1

answer = 0
z= z-2
visited=[[[0]*m for i in range(n)] for i in range(z+1)]

while h:

    cnt,move,x,y = heappop(h)
    c+=1
    if [x,y]==[n-1,m-1]:
        answer = cnt
        break

    if move==k:
        continue
    
 
    for i in range(4):
        a = x+dx[i]
        b = y+dy[i]

        if (0<=a<n and 0<=b<m)and not visited[cnt][a][b]:
            if arr[a][b]=='#':
                continue
        
            if arr[a][b]=='F' and move == k-1: # 숲으로 가면서 이동 가능 거리를 다  소모 할  경우
                continue

            if arr[a][b] =='.' or 'F':
                visited[cnt][a][b] = k
                heappush(h,[cnt,move+1,a,b])
            
            if cnt<z:
                if arr[a][b] =='.':
                    visited[cnt+1][a][b] =k
                    heappush(h,[cnt+1,0,a,b])



            
            
            
            
            
            
        
            
            
    





