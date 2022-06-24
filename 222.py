from collections import deque,defaultdict

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(n)]
blizard = [list(map(int,input().split())) for i in range(m)]
sx,sy = (n-1)//2,(n-1)//2

arr[sx][sy] = 9

dx = [0,-1,+1,0,0]
dy = [0,0,0,-1,1]

cnt_dic = defaultdict(int)


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

def search_explosion_group(loop):
    d = deque()
    d.append([sx,sy-1,arr[sx][sy-1]])
    explosion = []
    exp = [[sx,sy-1]]
    if arr[sx][sy-1] == 0:
        return False
    while d:
        x,y,num = d.popleft()
        dir = reverse_dir(direction[x][y])
        a = x+dx[dir]
        b = y+dy[dir]
        if 0<=a<n and 0<=b<n:
            if arr[a][b] == num:
                exp.append([a,b])
            else:
                if len(exp)>=4: # 폭발할 구슬 그룹이 있다는 뜻
                    print('ex',len(exp))
                    for ex_x, ex_y in exp:     
                        cnt_dic[arr[ex_x][ex_y]]+=1
                        arr[ex_x][ex_y] = 0
                    e = exp[-1]
                    d_zero.append(e)
                    explosion.append(e) # 제출할떄는 지워도됨. 폭발하는 구슬 확인용
                exp=[[a,b]]

            d.append([a,b,arr[a][b]])
    if d_zero:
        return True
    return False
        

def move_gooseul():

    while d_zero:
        x,y = d_zero.popleft()
        # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # print('x','y',x,y)
        dir = reverse_dir(direction[x][y])
    
        a = x + dx[dir]
        b = y + dy[dir]

        if a==sx and b ==sy:
            break
        
        if 0<=a<n and 0<=b<n and arr[a][b]:
    
            arr[x][y] = arr[a][b]
            arr[a][b] = 0
            d_zero.appendleft([a,b])
            tmp = deque()
            tmp.append([x,y])
    
            while tmp:

                x,y = tmp.popleft()
            
                dir = direction[x][y]
                if visited[x][y] == 2:
                    dir = next_dir(dir)
                p = x + dx[dir]
                q = y + dy[dir]
                if p==sx and q ==sy:
                    break
            
                if not arr[p][q]:
                    # print(p,q)
                    arr[p][q] = arr[x][y]
                    arr[x][y] = 0
                    tmp.append([p,q])
    

direction = [[0]*n for i in range(n)]
visited = [[0]*n for i in range(n)]



num = n*n - 1 
dir = 4
visited[0][0] = 1 
direction[0][0] = dir


d = deque()
d.append([0,0])

num -= 1

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


def is_go(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

# cnt_dic[arr[attack_x][attack_y]]+=1 구슬 폭발 

for d,s in blizard:
    attack_x , attack_y = sx,sy
    d_zero = deque()
    for _ in range(s):
        if is_go(attack_x+dx[d],attack_y+dy[d]):
            attack_x = attack_x+dx[d]
            attack_y = attack_y+dy[d]  
        else:
            break    
    
        
        arr[attack_x][attack_y] = 0

        d_zero.append([attack_x,attack_y])


    while d_zero:
        x,y = d_zero.popleft()
        dir = reverse_dir(direction[x][y])
        
        a = x + dx[dir]
        b = y + dy[dir]
        if 0<=a<n and 0<=b<n:
            arr[x][y] = arr[a][b]
            arr[a][b] = 0
            d_zero.append([a,b])

    
    # for z in arr:
    #     print(z)
    loop = True
    while loop:
        d_zero = deque()

        if search_explosion_group(loop):
            move_gooseul()
        else:
            loop = False
            break
        # for z in arr:
        #     print(z)


    

    d = deque()

    d.append([sx,sy-1,arr[sx][sy-1]])
    devide = deque()
    group_cnt = 1
    while d:
        x,y,num = d.popleft()
        if arr[x][y] == 0:
            break
        dir = reverse_dir(direction[x][y])
        a = x+dx[dir]
        b = y+dy[dir]
        if 0<=a<n and 0<=b<n:
            if arr[a][b] == num:
                group_cnt+=1
            else:
                A = group_cnt
                B = num
                devide.append(A)
                devide.append(B)
                group_cnt=1

            d.append([a,b,arr[a][b]])

    new_arr=[[0]*n for i in range(n)]

    if arr[sx][sy-1] != 0:
        

        d = deque()
        d.append([sx,sy-1])
        new_arr[sx][sy-1] = devide.popleft()

        while d:
            x,y = d.popleft()
            gooseul = devide.popleft()
            dir = reverse_dir(direction[x][y])
            a = x+dx[dir]
            b = y+dy[dir]
            if 0<=a<n and 0<=b<n:
                new_arr[a][b] = gooseul
                d.append([a,b])
            else:
                break 

            if not devide:
                break

        arr = new_arr


print(cnt_dic)

print(1*cnt_dic[1] + 2*cnt_dic[2] + 3*cnt_dic[3])
