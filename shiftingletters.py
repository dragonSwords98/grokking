
# Contributed by: Bryan Ling

class Solution:

    ALPHABET_LENGTH = 26

    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        accumulatedMove = 0
        result = ""
        shifts = shifts[::-1]
        for idx, item in enumerate(reversed(s)):

            # Determine how much shifting to 'accumulate'
            accumulatedMove += shifts[idx]

            # Determine the current character
            if ord(item) < 97 or ord(item) > 122:
                return ValueError(f"Letter provided in string (s) was not a lowercase alphabet: {ss}")

            # Shift this character, without overshifting the alphabet
            toShift = ord(item) + accumulatedMove % self.ALPHABET_LENGTH
            if toShift > 122:
                toShift = 96 + (toShift%122)
            result += chr(toShift)
            print(f"Shift {item} to {result[-1]} from {toShift} movements")

        return result[::-1]

        # ord('a') -> 97
        # chr(97) -> 'a'
        # chr(122) -> 'z'
        # '123' -> 'a'

        
def testSolution(s: str, shifts: list[int], expected: str) -> bool:
    solution = Solution()
    res = solution.shiftingLetters(s, shifts)
    print(res)
    assert expected == res, f"Expected {expected}, got {res}"

testSolution(s="abc",shifts=[3,5,9],expected="rpl")
testSolution(s="aaa",shifts=[1,2,3],expected="gfd")
testSolution(s="bad",shifts=[10,20,30],expected="jyh")
testSolution(s="ruu",shifts=[26,9,17],expected="rul")