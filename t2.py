from collections import defaultdict,deque



#R T
#C F
#J M
#A N

def solution(queue1,queue2):
    from collections import deque
  
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    s1,s2 = sum(queue1),sum(queue2)

    if s1==s2:
        return 0
    else:
        
        answer = -2 
        cnt = 0

        upper = 300000
        while cnt<upper:
            if s1>s2:
                x = deq1.popleft()
                s1 -= x
                y = deq2.append(x)
                s2 += x
            else:
                x = deq2.popleft()
                s2 -= x
                y = deq1.append(x)
                s1 += x
            cnt +=1 
   
            if s1==s2: 
                answer = cnt
                
                return answer
               
    return -1


# def solution(survey,choices):
#     from collections import defaultdict
#     dic = defaultdict(int)
#     answer = ""
#     for i,j in zip(survey,choices):
#         left,right = list(i)
        
#         if j-4<0:
#             score = 4-j
#             dic[left]+= score
#         elif j-4>0:
#             score = j-4
#             dic[right]+=score
#         else:
#             pass
#     answer = ""
#     arr =[["R T"],["C F"],["J M"],["A N"]]

#     for i in arr:
#         x,y = i[0].split()
#         if dic[x]<dic[y]:
#             answer+=y
#         elif dic[x]>dic[y]:
#             answer+=x
#         else:
#             if ord(x)>ord(y):
#                 answer+=y
#             else:
#                 answer+=x

#     return answer




from collections import deque
# def solution(queue1,queue2):
#     answer = -1
#     d1,d2= deque(queue1),deque(queue2)
    
#     if sum(queue1)==sum(queue2):
#         return 0
#         # return answer
#     else:
#         sum_q1,sum_q2 = sum(queue1),sum(queue2)
#         count = 0
     
#         while count<300_000:
#             if sum_q1>sum_q2:
#                 x = d1.popleft()
#                 sum_q1 -= x
#                 y = d2.append(x)
#                 sum_q2 += x
#             else:
#                 x = d2.popleft()
#                 sum_q2 -= x
#                 y = d1.append(x)
#                 sum_q1 += x
#             count +=1 

#             if sum_q1==sum_q2: 
#                 answer = count
#                 return answer

#     return answer