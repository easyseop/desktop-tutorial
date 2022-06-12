def solution(n,paths,gates,summits):
    from heapq import heappush,heappop
    from collections import defaultdict,deque
    min_cost = [i[2] for i in paths]
    print(min_cost)
    dic = defaultdict(list)
    for i,j,c in paths:
        dic[i].append([j,c])
        dic[j].append([i,c])

    real_answer_node ,real_answer_intensity = 50000+1,10000000+1

    for s in summits:
        print('s==========')
        # reach_goal = False
        answer_intensity = 10000000+1
        answer_node = 50000+1
        
        h  = []
        heappush(h,[0,s])
        visited =[]
        visited.append([0,s])
    
        while h:
            intensity,curr_node = heappop(h)

            if curr_node in gates:
      
                if answer_intensity>intensity:
                    answer_intensity = intensity
                    answer_node = s
                    break
                elif answer_intensity == intensity:
                    answer_node = min(answer_node,s)
                    break
                else:
                    pass

            for next_node,cost in dic[curr_node]:
        
                cost  = max(intensity,cost)

                if next_node in summits:
                    continue

                else:
                    if [cost,next_node] not in visited:
                      
                        visited.append([cost,next_node])
                        heappush(h,[cost,next_node])        

        


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



