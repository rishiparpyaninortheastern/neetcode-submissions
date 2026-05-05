class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        visiting=set()
        visited=set()
        validans=[]

        for course,prereq in prerequisites:
            graph[course].append(prereq)
        
        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            visiting.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):  # ← propagate False
                    return False
            visiting.remove(course)
            visited.add(course)
            validans.append(course)
            return True

        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return validans

        