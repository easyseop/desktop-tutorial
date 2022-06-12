def solution(n,paths,gates,summits):
    from heapq import heappush,heappop
    
    from collections import defaultdict,deque
    from copy import deepcopy
    min_cost = [i[2] for i in paths]
    
    dic = defaultdict(list)
    for i,j,c in paths:
        dic[i].append([j,c])
        dic[j].append([i,c])

    real_answer_node ,real_answer_intensity = 50000+1,10000000+1

    for gate in gates:

        # reach_goal = False
        answer_intensity = 10000000+1
        answer_node = 50000+1
        
        h  = []
        visited =[0]*(n+1)
        visited[gate] = 1
        heappush(h,[0,gate,visited])
        visited =[0]*(n+1)
        visited[gate] = 1
        
    
        while h:
            intensity,curr_node,visited = heappop(h)
           
            if curr_node in summits:
          
                if answer_intensity>intensity:
                    answer_intensity = intensity
                    answer_node = curr_node
                    break
                elif answer_intensity == intensity:
                    answer_node = min(answer_node,curr_node)
                    break
                else:
                    pass

            for next_node,cost in dic[curr_node]:
                
                cost  = max(intensity,cost)

                if next_node in gates:
                    continue

                else:
                    if not visited[next_node]:
                        new_v = deepcopy(visited)
                        new_v[next_node] = 1
                        heappush(h,[cost,next_node,new_v])        

        


        if real_answer_intensity>answer_intensity:
 
            real_answer_intensity=answer_intensity
            real_answer_node = answer_node

        elif real_answer_intensity == answer_intensity:
            real_answer_node = min(real_answer_node,answer_node)
        else:
            pass
            
        if real_answer_intensity==min_cost:
            return [real_answer_node,real_answer_intensity]

    return [real_answer_node,real_answer_intensity]

n = 7
paths = [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]
gates = [1,2]
summits = [5]
print(solution(n,paths,gates , summits))