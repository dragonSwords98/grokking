class Solution:

    BLANK_CHESS_BOARD = [[".",".","Q",".",".",".",".","."],
                        [".",".",".",".",".",".","Q","."],
                        [".",".",".",".","Q",".",".","."],
                        ["Q",".",".",".",".",".",".","."],
                        [".",".",".",".",".","Q",".","."],
                        [".",".",".","Q",".",".",".","."],
                        [".","Q",".",".",".",".",".","."],
                        [".",".",".",".",".",".",".","."]]

    _board = BLANK_CHESS_BOARD
    solutions = []


    def provideNonAttackingQueenCombinations(self, board: list[list[str]]) -> list:
        """
        1. Assume a queen to each column and only shift those queens along their designated column to find solutions.
        2. try rotating the empty columns in place to find more solutions
        3. once a solution is found, rotate the board 90 deg, 180 deg, 270 deg to find its permutations
        """
        self._board = board

        for yIndex in range(1, 9):
            for xIndex in range(1, 9):
                # TODO: this double for loop shifting does not COVER all possiblities
                self.shiftQueenLeft(xIndex, yIndex)
                if self.testBoard() and self.notDuplicateBoard():
                    # found a unique solution
                    self.solutions.append(self._board)

    def shiftQueenLeft(self, xIndex, yIndex):
        back = self._board[yIndex][xIndex].pop()
        self._board[yIndex][xIndex].insert(0, back)
        return

    def getColumn(self, xIndex):
        return [i[xIndex] for i in self._board]

    def getDiagonals(self, xIndex, yIndex):
        diagonals = []
        _xIndex = xIndex
        _yIndex = yIndex
        while _xIndex >= 0 and _yIndex >= 0:
            _xIndex -= 1
            _yIndex -= 1
            diagonals.append(self._board[_xIndex, _yIndex])
        
        _xIndex = xIndex
        _yIndex = yIndex
        while _xIndex < 9 and _yIndex < 9:
            _xIndex += 1
            _yIndex += 1
            diagonals.append(self._board[_xIndex, _yIndex])
                


    def testBoard(self):
        for yIndex in range(1, 9):
            foundQueen = False
            for xIndex in range(1, 9):
                if self._board[yIndex][xIndex] == "Q":
                    if foundQueen:
                        return False
                    foundQueen = True

                    if "Q" in self.getColumn(xIndex):
                        return False

                    if "Q" in self.getDiagonals(yIndex, xIndex):
                        return False
                
                    return True

    def notDuplicateBoard(self):
        return self._board not in self.solutions # not a legit code, but intent is here
        
class Answer:
    def queens(self, n, i, a, b, c):
        if i < n:
            for j in range(n):
                if j not in a and i+j not in b and i-j not in c:
                    yield from self.queens(n, i+1, a+[j], b+[i+j], c+[i-j])
        else:
            yield a
    
    def rooks(self, n, i, a):
        if i < n:
            for j in range(n):
                if j not in a:
                    yield from self.rooks(n, i+1, a+[j])
        else:
            yield a


answer = Answer()
queenCount = 0
for solution in answer.queens(9, 0, [], [], []):
    queenCount += 1
    print(solution)

# rookCount = 0
# for solution in answer.rooks(8, 0, []):
#     rookCount += 1
#     print(solution)
# this is 8! solutions because of rooks behavior and factorial

print(queenCount)
# print(rookCount)