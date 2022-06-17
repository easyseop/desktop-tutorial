from collections import deque
n , m = map(int,input().split())

arr = [list(map(int,input().split()))  for i in range(n)]

dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,+1,+1,+1,0,-1]

daegaksun_x = [-1,-1,1,1]
daegaksun_y = [-1,+1,-1,1]

order_list = [list(map(int,input().split())) for i in range(m)]

d = deque(order_list)
d_groom = deque([[n-1,0] ,[n-1,1],[n-2,0] ,[n-2,1]])


visited = [[0]*n for i in range(n)]



def dir(x,y):
    if x>=n:
        x=x%n
    elif x<0:
        while x<0:
            x+=n
    if y>=n:
        y=y%n
    if y<0:
        while y<0:
            y+=n
    return x,y

    
# print(two_over)

while d:
    visited = [[0]*n for i in range(n)]
    direction,distance  = d.popleft()
    # print('ddd',direction)
    move_x,move_y = dx[direction-1],dy[direction-1]
    no_groom = []
    # print(d_groom)
    for i in range(len(d_groom)):
        x,y = d_groom.popleft()

        x,y = dir(x+move_x*distance,y+move_y*distance)

        arr[x][y] += 1
   
        d_groom.append([x,y])
        visited[x][y] = 1

    while d_groom:

        a,b = d_groom.popleft()
 
        water_plus = []
        cnt= 0 

        for j in range(4):
            # print(j)
            new_a = a+daegaksun_x[j]
            new_b = b+daegaksun_y[j]
            if 0<=new_a<n and 0<=new_b<n:
                if arr[new_a][new_b]>=1:
                    cnt+=1 
        arr[a][b]+= cnt
    
    for p in range(n):
        for q in range(n):
            if not visited[p][q] and arr[p][q]>=2:

                arr[p][q] -= 2
                d_groom.append([p,q])

answer = 0    
for i in range(n):
    for j in range(n):
        answer+=arr[i][j]
print(answer)

    

    

    





