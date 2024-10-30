def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    visit_status = [0] * numCourses

    def dfs(course):
        if visit_status[course] == 1:  # Cycle detected
            return False
        if visit_status[course] == 2:  # Already visited
            return True

        visit_status[course] = 1  # Mark as visiting
        for next_course in graph[course]:
            if not dfs(next_course):
                return False

        visit_status[course] = 2  # Mark as visited
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True

# Example Execution
numCourses_example = 2
prerequisites_example = [[1, 0]]
print("Course Schedule Result:", canFinish(numCourses_example, prerequisites_example))
