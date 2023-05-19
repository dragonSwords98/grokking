# Contributed by: Bryan Ling

from collections import OrderedDict

class Solution:

    def findWinnersSlower(self, matches: list[list[int]]) -> list[list[int]]:

        # take matches and reduce directly into an answer
        answer = {}
        eliminated = []

        for winner, loser in matches:

            # if not a double loser, say they're unbeaten
            if winner not in answer[0]:
                if winner not in eliminated and winner not in answer[1]:
                    answer[0].append(winner)
            
            if loser not in eliminated:
                if loser in answer[0]:
                    # move loser from winner to 1 loss
                    answer[0].remove(loser)
                    answer[1].append(loser)
                elif loser in answer[1]:
                    # move loser to eliminated
                    answer[1].remove(loser)
                    eliminated.append(loser)
                else:
                    answer[1].append(loser)
            
        return [sorted(answer[0]), sorted(answer[1])]
        

    def findWinnersOrderedDict(self, matches: list[list[int]]) -> list[list[int]]:
        players = OrderedDict()
        answer = [[],[]]
        for winner, loser in matches:
            
            # loser gets +1
            if loser in players:
                players[loser] += 1
            else:
                players.setdefault(loser, 1)
                
            # winner gets 0 or no increase in losses
            players.setdefault(winner, 0)
            
        # only unbeatable or one-losses left
        players = {k:v for (k,v) in players.items() if v <= 1}
        
        for k in players.keys():
            if players[k] == 0:
                answer[0].append(k)
            elif players[k] == 1:
                answer[1].append(k)

        return answer


    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        players = {}
        answer = [[],[]]
        for m in matches:
            winner = m[0]
            loser = m[1]
            
            # loser gets +1
            if loser in players:
                players[loser] += 1
            else:
                players.setdefault(loser, 1)
                
            # winner gets 0 or no increase in losses
            players.setdefault(winner, 0)
            
        # only unbeatable or one-losses left
        players = {k:v for (k,v) in players.items() if v <= 1}
        
        for k in sorted(players.keys()):
            if players[k] == 0:
                answer[0].append(k)
            elif players[k] == 1:
                answer[1].append(k)

                
        return answer
  
    ## LEETCODE SOLUTION MATCHES THIS, WHICH YOU WERE ABLE TO COME UP WITH YOURSELF (Y)
    # O(n log n) runtime, due to the sorting of two sets at the end, the iteration over matches is O(n), all ifs are O(1)
    # O(n) memory due to 3 sets adding up to n matches
    def findWinnersSet(self, matches: list[list[int]]) -> list[list[int]]:
        won = set()
        loss = set()
        eliminated = set()

        for winner, loser in matches:
            # winners are always added
            # a loser is removed from unbeaten
            if winner not in eliminated and winner not in loss:
                won.add(winner)
            
            won.discard(loser)

            # losers could be added to loss or elminated
            if loser not in loss and loser not in eliminated:
                loss.add(loser)
            else:
                eliminated.add(loser)
                loss.discard(loser)

        return [sorted(list(won)), sorted(list(loss))]

# answer[0] = unbeatable (no losses)
# answer[1] = one loss

# only consider players who have played 1+ matches
# lists must be in increasing order

# no 2 matches have the same outcome

# could be up to 1 million players



# so add to a ordered list
# iterate the list after

# 1,000,000 matches 2x

# O(2n) => O(n)

# 1. parse all matches
# 2. parse your hashmap after



A = Solution().findWinnersSet([[2,3],[1,3],[5,4],[6,4]])
print(A)
assert A == [[1,2,5,6],[]]

B = Solution().findWinnersSet([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
print(B)
assert B == [[1,2,10],[4,5,7,8]]

C = Solution().findWinnersSet([[1,2],[2,1]])
print(C)
assert C == [[],[1,2]]