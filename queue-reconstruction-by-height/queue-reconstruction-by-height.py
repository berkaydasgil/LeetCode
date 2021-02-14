class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        for p in sorted(people, key= lambda x:[-x[0],x[1]]):
            queue.insert(p[1],p)
        return queue
        