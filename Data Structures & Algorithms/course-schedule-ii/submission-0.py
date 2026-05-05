from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        validans = []
        visiting = set()
        visited = set()
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(course):
            if course in visiting:
                return False  # cycle detected
            if course in visited:
                return True   # already safe

            visiting.add(course)
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False  # propagate cycle
            visiting.remove(course)
            visited.add(course)
            validans.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []  # cycle detected, return empty list

        return validans
