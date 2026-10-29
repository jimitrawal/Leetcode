from collections import deque 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indeg = [0]*numCourses
        q = deque()
        for i in range(len(prerequisites)):
            if prerequisites[i][1] == prerequisites[i][0]:
                return False
            indeg[prerequisites[i][0]] += 1
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        while q:
            for c, pre in prerequisites:
                if pre == q[0]:
                    indeg[c] -= 1
                    if indeg[c] == 0:
                        q.append(c)
            q.popleft()
          #indeg = [0, 0, 0, 0, 0] 
          #q = [] 
        if not(indeg == [0]*numCourses):
            return False
        return True