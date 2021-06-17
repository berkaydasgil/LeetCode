

class Solution:
    def numTrees(self, n: int) -> int:
        tree=[1] * (n+1)
        for nodes in range(2,n+1):
            total = 0
            for pivot in range(1,nodes+1):
                L = tree[pivot-1]
                R = tree[nodes-pivot]
                total += L*R
            tree[nodes]=total
        return tree[n]  
