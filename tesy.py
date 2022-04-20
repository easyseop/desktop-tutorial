n = int(input())
arr = [int(input()) for i in range(n)]
stack = []
ans = []
pop = []
j= 0
flag = arr[j]


for i in range(1,n+1):
    stack.append(i)
    ans.append('+')
    if  stack[-1] == flag:
        while stack:
            flag = arr[j]
            if stack[-1] == flag:
                pop.append(stack.pop())
                ans.append('-')
                j+=1
                
            else:
                break
        

print(ans)
print(pop)
print(arr)



            
