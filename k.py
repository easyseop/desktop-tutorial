def solution():
    N,M = map(int,input().split())
    ans = 0
    arr = [i%2 for i in list(map(int,input().split()))] #짝수면 0 홀수면 1


    can_minus=  M

    dp = [0] * (N)
    start,end = 0,1

    even = 0

    if arr[start] ==0:
        even+=1
    else:
        can_minus -= 1
    ans = even

    if N ==1:
        return ans
  
    while end<N:
        print('start',start,'end',end)
        if arr[end]==0:
            even += 1
        else:
            can_minus-=1
            print('can_minus',can_minus)
        if can_minus>=0:
            end+=1
        else:
            while can_minus<0:

                if start == N or start==end:
                    break
                if arr[start]==0:
                    even -= 1
                else:
                    can_minus +=1
                start+=1      
      
            end+=1
        
        print('eveb',even)
        
        ans = max(ans,even)
    return ans
        

s = solution()
print(s)


    



