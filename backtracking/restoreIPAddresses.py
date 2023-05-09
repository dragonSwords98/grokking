
# constraints: 
# <13 digits
# <=255255255255
# >3 digits
# if its all zeroes, and it must have 4 zeroes and exactly 4.


# you're organizing 3 dots into a string

# 3 dots use them as 'runners', running until all possiblities are covered

# 2.5.5.255255255 -> 255255255.2.5.5

# 1.1.1.1 -> 1.1.1.1

# 1.2.1.2121 -> first legal is 1.2.12.121
# last legal is 121.12.2.1
# 3.4.5.67

# from copy import deepcopy
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Store all addresses in res
        res = []
        
        def BT(i,address):
            print(i, address)
            # No more digit, so no more state can be generated.
            if i==len(s):
                print("approvin...", address)
                # It is possible that the address contains less than 4 numbers
                # We only store the valid ones.
                if len(address)==4:
                    res.append( '.'.join(map(str,address)) )
                return
            
            # If the last number is not 0, we can add the new digit to it (no leading zero)
            # After adding the new digit, the number has to be <= 255.
            if address[-1]!=0 and address[-1]*10+int(s[i]) <= 255:
                lastItem = address[-1]
                print("change state", address[-1], " to ", lastItem*10+int(s[i]))
                address[-1] = lastItem*10+int(s[i]) #change the current state to its neighboring state
                BT(i+1, address)                    #backtrack(state)
                print("back tracking", address[-1], " to ", lastItem, address)
                address[-1] = lastItem              #restore the state (backtrack)
            
            # The address can not contain more than 4 numbers.
            if len(address)<4:
                print("address too short, lets keep going if we can: add", int(s[i]), "to ", address)
                address.append(int(s[i]))           #change the current state to its neighboring state
                BT(i+1,address)         #backtrack(state)
                print("backtracking", address[-1], address)
                address.pop()                       #restore the state (backtrack)
        
        BT(1,[int(s[0])])
        return res
    # def restoreIpAddresses(self, s: str) -> list:
    #     result = []
    #     INIT_DOT_INDICES = [1, 3, 5]

    #     # 0. do constraint check on str
    #     if len(s) > 12 or int(s) > 255255255255 or len(s) < 3 or (int(s) == 0 and len(s) != 4):
    #         return []

    #     # 1. place 3 dots
    #     dotIndices = INIT_DOT_INDICES

    #     # 2. determine if 3 dots are legal
    #     # 3. slide until legal
    #     while not self.isLegalIp(s, dotIndices):
    #         dotIndices = self.slideDotIndicesToNextPossiblePos(s, dotIndices)
    #         if dotIndices is None:
    #             return result
        
    #     # 4. Record end indices to know when to stop
    #     endIndices = self.computeInverseIndices(s, dotIndices)
    #     result.append(dotIndices)

    #     # 5. compute all running possibilities until the dots are in the -1 index pos of where it started, aka if start at [2], it should end at [-2] (*capture the start indices and compute the end indices from there)
    #     while set(dotIndices) != set(endIndices):
    #         dotIndices = self.slideDotIndicesToNextPossiblePos(s, dotIndices)
    #         if dotIndices is None:
    #             return result
    #         if self.isLegalIp(s, dotIndices):
    #             result.append(dotIndices)

    #     return result

    # def isLegalLengths(self, s: str, dotIndices: list):
    #     if dotIndices[0] > 3 or dotIndices[1] - dotIndices[0] > 3 or dotIndices[2] - dotIndices[1] > 3 or len(s) - dotIndices[2] > 3:
    #         return False
    #     return True

    # def isLegalIp(self, s: str, dotIndices: list):
    #     if 0 < int(s[:dotIndices[0]]) > 255 or 0 < int(s[dotIndices[1]:dotIndices[2]]) > 255 or 0 < int(s[dotIndices[2]:]) > 255:
    #         return False
    #     return True

    # def slideDotIndicesToNextPossiblePos(self, s: str, dotIndices: list):

    #     # TODO: fix this. it does not slide properly

    #     clone = dotIndices.copy()
    #     if (self.isLegalLengths(s, clone)):
    #         return clone
    #     while clone[2] < len(s) - 1:
    #         clone[2] += 1
    #         if (self.isLegalLengths(s, clone)):
    #             return clone
    #     clone[2] = dotIndices[2]
    #     while clone[1] < len(s) - 1:
    #         clone[1] += 1
    #         if (self.isLegalLengths(s, clone)):
    #             return clone
    #     clone[1] = dotIndices[1]
    #     while clone[0] < len(s) - 1:
    #         clone[0] += 1
    #         if (self.isLegalLengths(s, clone)):
    #             return clone
    #     clone[0] = dotIndices[0]
    #     return None
    
    # def computeInverseIndices(self, s: str, dotIndices: list):
    #     dotIndices[0] = len(s) - 1 - dotIndices[0]
    #     dotIndices[1] = len(s) - 1 - dotIndices[1]
    #     dotIndices[2] = len(s) - 1 - dotIndices[2]
    #     return dotIndices


A = Solution().restoreIpAddresses("25525511135")
print(A)
assert A.sort() == ["255.255.11.135","255.255.111.35"].sort()

# B = Solution().restoreIpAddresses("0000")
# print(B)
# assert B.sort() == ["0.0.0.0"].sort()

# C = Solution().restoreIpAddresses("101023")
# print(C)
# assert ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"].sort() == C.sort()

