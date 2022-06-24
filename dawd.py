from collections import deque,defaultdict
def next_dir(dir):
    if dir==4:
        return 2
    elif dir==2:
        return 3
    elif dir==3:
        return 1
    else:
        return 4

def reverse_dir(dir):
    if dir==4:
        return 3
    elif dir==2:
        return 1
    elif dir==3:
        return 4
    else:
        return 2

def set_direction():
    num = n*n - 1 
    d = deque()
    d.append([0,0])
    num -= 1
    dir = 4
    while d:  
        x,y = d.popleft()

        if x==sx and y == sy:
            break

        a = x+dx[dir]
        b = y+dy[dir]
        if 0<=a<n and 0<=b<n and not visited[a][b]: 
            d.append([a,b])
            visited[a][b] = 1
            direction[a][b] = dir
            # number[a][b] = num
            num -= 1
        else:
            dir = next_dir(dir)
            visited[x][y] = 2 # 2는 방향 전환을 의미 
            a = x+dx[dir]
            b = y+dy[dir]
            if 0<=a<n and 0<=b<n and not visited[a][b]:
                
                d.append([a,b])
                visited[a][b] = 1
                direction[a][b] = dir
                # number[a][b] = num
                num -= 1

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]
blizard = [list(map(int,input().split())) for i in range(m)]
sx,sy = (n-1)//2,(n-1)//2

arr[sx][sy] = 9

dx = [0,-1,+1,0,0]
dy = [0,0,0,-1,1]


cnt_dic = defaultdict(int)

    
direction = [[0]*n for i in range(n)]
visited = [[0]*n for i in range(n)]


visited[0][0] = 1 
direction[0][0] = 4

set_direction()

for d,s in blizard:
    attack_x , attack_y = sx,sy
    d_zero = deque()
    for _ in range(s):
        if 0<=attack_x+dx[d]<n and 0<= attack_y+dy[d] <n:
            attack_x = attack_x+dx[d]
            attack_y = attack_y+dy[d]  
        else:
            break        
        arr[attack_x][attack_y] = 0

    one_dim_arr = [0]*(n**2)
    d=deque()
    d.append([sx,sy-1])
    idx = 1
    one_dim_arr[idx] = arr[sx][sy-1]


    while d:
        idx+=1
        if idx ==n**2:
            break
        x,y = d.popleft()
        dir = reverse_dir(direction[x][y])
        a=x+dx[dir]
        b=y+dy[dir]
        one_dim_arr[idx] = arr[a][b]
        d.append([a,b])

    while 1:
        flag = False
        explosion = [[1,one_dim_arr[1]]] #idx, value
        num = one_dim_arr[1]
        for i in range(2,n**2):
            if one_dim_arr[i] == 0:
                continue
            if one_dim_arr[i] == num:

                explosion.append([i,num])
            else:
                if len(explosion)>=4:
                    flag = True
                    while explosion:
                        idx,value = explosion.pop()
                    
                        one_dim_arr[idx]=0
                        cnt_dic[value] += 1
             
                explosion = []
                num = one_dim_arr[i]
                explosion.append([i,one_dim_arr[i]])

        if i==n**2-1:
            if len(explosion)>=4:
                flag = True
  
                while explosion:
                    idx,value = explosion.pop()
                    one_dim_arr[idx]=0
                    cnt_dic[value] += 1
    

        if not flag:
            break
   
    new_arr = [[0]*n for i in range(n)]
    new_x,new_y = sx,sy-1

    devide = 0
    flag = True

    for i in range(n**2):
        if one_dim_arr[i] == 0:
            continue
        if devide==0:
            num = one_dim_arr[i]
            devide +=1 
        else:
            if num == one_dim_arr[i]:
                devide += 1
            else:
                A,B = devide,num
                new_arr[new_x][new_y]=A
                dir = reverse_dir(direction[new_x][new_y])
                new_x,new_y =new_x+dx[dir] , new_y+dy[dir]
                if new_x ==0 and new_y ==0:
                    flag=False
                    break
                new_arr[new_x][new_y]=B
                dir = reverse_dir(direction[new_x][new_y])
                new_x,new_y =new_x+dx[dir] , new_y+dy[dir]
                devide = 1
                num = one_dim_arr[i]
                if new_x ==0 and new_y ==0:
                    flag=False
                    break
    if flag:
        A,B = devide,num
        new_arr[new_x][new_y]=A
        dir = reverse_dir(direction[new_x][new_y])
        new_x,new_y =new_x+dx[dir] , new_y+dy[dir]
        new_arr[new_x][new_y]=B
    

    arr = new_arr

print(1*cnt_dic[1] + 2*cnt_dic[2] + 3*cnt_dic[3])
    
    


        
    
    



