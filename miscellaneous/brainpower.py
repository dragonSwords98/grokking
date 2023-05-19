# Written by Bryan to solve Leetcode problem

###
# BRAINSTORMING, what I was thinking in order to figure this out
# this is a knapsack problem in disguise

# no, this is a graph problem in disguise

# open a new path for each node that isn't on a path, until you've found all paths
# determine which 'path' earns you the most points

# perform DFS until all nodes are visited
# record the path with the highest points found

#iterative approach allows me to complete this in n time

# no... there's an even simpler answer

# visit the array backwards
# get the best score you can with each node, visit the nodes that it can visit and pick the max score you can get, record it
# contd til you visit all nodes once

# O(n) time, cause each time you look backwards, you're only referring to the lookup table for the max value found before
###

import itertools


class Solution:

    visited = []

    def mostPoints(self, questions: list[list[int]]) -> int:
        visited = list(itertools.repeat(0,len(questions)))

        for idx, q in enumerate(questions):
            points = q[0]
            brainpower = q[1]
            visited[idx] = max(visited[idx], points)
            for link in range(idx + brainpower + 1, len(questions)):
                visited[link] = max(visited[link], visited[idx] + questions[link][0])

            print(visited)

        return max(visited)
    

# import itertools


# class Solution:

#     visited = []

#     def mostPoints(self, questions: list[list[int]]) -> int:
#         visited = list(itertools.repeat(-1,len(questions)))
#         questions.reverse()
#         for idx, q in enumerate(questions):
#             points = q[0]
#             brainpower = q[1]

#             # collect the points now
#             if visited[idx] == -1:
#                 visited[idx] = points
#             else:
#                 visited[idx] = visited[idx] + points

#             # see if you can done better with the past (nodes later in the array which you already visited in reverse)
#             # you would never encounter a -1 going backwards, because you must visit nodes in order
#             # also after you already looked at the visited once
#             if idx - brainpower > 0 and idx - brainpower <= len(questions) - 1:
#                 visited[idx] = visited[idx] + max(visited[0: idx - brainpower])

#             print(visited)

#         return max(visited)

s = Solution()
t = [[3,2],[4,3],[4,4],[2,5]]
print(t.reverse())
print('Most points is', s.mostPoints([[43,5]]))
print('Most points is', s.mostPoints([[3,2],[4,3],[4,4],[2,5]]))
print('Most points is', s.mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))
print('Most points is', s.mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]))
print('Most points is', s.mostPoints([[21,2],[1,2],[12,5],[7,2],[35,3],[32,2],[80,2],[91,5],[92,3],[27,3],[19,1],[37,3],[85,2],[33,4],[25,1],[91,4],[44,3],[93,3],[65,4],[82,3],[85,5],[81,3],[29,2],[25,1],[74,2],[58,1],[85,1],[84,2],[27,2],[47,5],[48,4],[3,2],[44,3],[60,5],[19,2],[9,4],[29,5],[15,3],[1,3],[60,2],[63,3],[79,3],[19,1],[7,1],[35,1],[55,4],[1,4],[41,1],[58,5]]))


# this problem is exceeding the time limit on leetcode

# LEET CODE provided answer below:
# from typing import List
# class Solution:
#     def mostPoints(self, questions: List[List[int]]) -> int:
#         n = len(questions)
#         dp = [0] * (n+1)
#         for i in range(n-1, -1, -1):
#             point = questions[i][0]
#             jump = questions[i][1]

#             nextQuestion = min(n, i+jump+1)
#             dp[i] = max(dp[i+1], point + dp[nextQuestion])
#         return dp[0]
