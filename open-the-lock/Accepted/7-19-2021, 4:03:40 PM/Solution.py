// https://leetcode.com/problems/open-the-lock

from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if('0000' in deadends):
            return -1
        
        target = int(target)
        
        visited=[False]*10000
        for i in deadends:
            visited[int(i)]=True
        if visited[target]:
            return -1
        def count_steps(target,head):
            steps=0
            queue=deque([head])

            while(queue):
                curr_level=[]
                # print(queue)
                while(queue):
                    head=queue.popleft()
                    if(head >= 10000 or head < 0 or visited[head]):
                        continue
                    visited[head]=True
                    if(head==target):
                        return steps
                    for i in range(4):
                        start=head
                        if( start% (10**(i+1)) < 10**(i)):
                            start_up=start+10**i
                            curr_level.append(start_up)
                            start+=9*(10**i) 
                            curr_level.append(start)
                        elif(start % (10**(i+1)) >= 9* 10**(i)):
                            start_down=start-10**i
                            curr_level.append(start_down)
                            start-=9*(10**i)
                            curr_level.append(start)
                        else:
                            start_up=start+10**i
                            curr_level.append(start_up)
                            start_down=start-10**i
                            curr_level.append(start_down)
                steps+=1
                queue=deque(curr_level[::])
            return -1
        return count_steps(target, 0)
                    
# ["0201","0101","0102","1212","2002"]
# "0202"

                    
                
                
'''
0204
0294
'''

            

                
            
            
        
        
            
        
                        
        