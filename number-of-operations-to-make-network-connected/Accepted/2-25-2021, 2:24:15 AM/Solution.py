// https://leetcode.com/problems/number-of-operations-to-make-network-connected

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        parent = [i for i in range(n)]
        
        def find(i):
            while i != parent[i]:
                i = parent[i]
                parent[i] = parent[parent[i]]
            return i
        
        extra_wires = 0
        for i, j in connections:
            p_i = find(i)
            p_j = find(j)
            if p_i == p_j:
                extra_wires += 1
                continue
            parent[p_i] = p_j
        
        total_groups = 0
        for i in range(n):
            if parent[i] == i:
                total_groups += 1
                
        if total_groups - 1 > extra_wires:
            return -1
        return total_groups - 1
        
        
'''
n computers
0 to n-1

con[i] = [a, b]

'''