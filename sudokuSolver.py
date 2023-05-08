class Solution:
    ONE_TO_NINE = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    _board = []

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # find possiblities in each unsolved cell
        # reduced the possibilities by filling in single solution cells and redoing possiblities until none remain without 2+ possiblities
        # do trial n error with backtrackinig
        # as you try each cell, guess until you're wrong, erase and try, erase and try recursively until a solution yields
        # if a solution is fully possible, return it


        possiblities = []
        for a in board:
            unsolved = []
            for b in a:
                unsolved.append(self.getUnsolvedNumbersForCell(a, b, board))
            possibilpossiblitiesities.append(unsolved)
        
        return self.tryEachPossibilityUntilSucccess(possiblities)


    def displayPossibilities(self, board: List[List[str]]) -> List[List[str]]:
        """
        Return the board's possibilities
        """

    def tryEachPossibilityUntilSuccess(self, combinations):
        """
        Try each combination until success 

        Use backtracking, try numbers until fail, swap out and keep trying until success
        """
        return False
        
        
    def getRow(self, xIndex, yIndex, board) -> List[str]:
        return board[xIndex]

    def getColumn(self, xIndex, yIndex, board) -> List[str]:
        return board[:][yIndex]

    def getBox(self, xIndex, yIndex, board) -> List[str]:
        return board[:xIndex % 3][:yIndex % 3]

    def negate_intersect(a, b) => List[str]:
        return list(set(b) - set(a))

    def getUnsolvedNumbersForCell(self, xIndex, yIndex, board) -> List[str]:
        r = self.getRow(xIndex, yIndex, board)
        c = self.getColumn(xIndex, yIndex, board)
        b = self.getBox(xIndex, yIndex, board)

        unsolved = self.negate_intersect(r + c + b, self.ONE_TO_NINE)
        return unsolved

puzzles = [
    [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
    
    [["2","6",".",".","7",".",".",".","."],[".",".","9","6",".","2",".","1","."],["4",".",".","3",".",".",".",".","."],
    [".",".","3",".",".",".",".",".","8"],["8",".","7","9",".","4","5",".","2"],["9",".",".",".",".",".","7",".","."],
    [".",".",".",".",".","7",".",".","5"],[".","4",".","2",".","6","1",".","."],[".",".",".",".","3",".",".","8","6"]],

    [["6",".",".",".",".",".","8",".","3"],[".","4",".","7",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],
    [".",".",".","5",".","4",".","7","."],["3",".",".","2",".",".",".",".","."],["1",".","6",".",".",".",".",".","."],
    [".","2",".",".",".",".",".","5","."],[".",".",".",".","8",".","6",".","."],[".",".",".",".","1",".",".",".","."]],

    [[".",".","5",".",".",".","9","8","7"],[".","4",".",".","5",".",".",".","1"],[".",".","7",".",".",".",".",".","."],
    ["2",".",".",".","4","8",".",".","."],[".","9",".","1",".",".",".",".","."],["6",".",".","2",".",".",".",".","."],
    ["3",".",".","6",".",".","2",".","."],[".",".",".",".",".","9",".","7","."],[".",".",".",".",".",".","5",".","."]],

    [[".",".",".",".",".",".",".","7","1"],[".","2",".","8",".",".",".",".","."],[".",".",".","4",".","3",".",".","."],
    ["7",".",".",".","6",".",".","5","."],[".",".",".","2",".",".","3",".","."],["9",".",".",".",".",".",".",".","."],
    ["6",".",".",".","7",".",".",".","."],[".","8",".",".",".",".","4",".","."],[".",".",".",".","5",".",".",".","."]],

    [[".","4","7",".","8",".",".",".","1"],[".",".",".",".",".",".",".",".","."],[".",".",".","6",".",".","7",".","."],
    ["6",".",".",".",".","3","5","7","."],[".",".",".",".",".","5",".",".","."],[".","1",".",".","6",".",".",".","."],
    ["2","8",".",".","4",".",".",".","."],[".","9",".","1",".",".",".","4","."],[".",".",".",".","2",".","6","9","."]],

    [[".","2",".",".",".",".",".",".","."],["3",".","5",".","6","2",".",".","9"],[".","6","8",".",".",".","3",".","."],
    [".","5",".",".",".",".",".",".","."],[".",".",".","6","4",".","8",".","2"],[".",".","4","7",".",".","9",".","."],
    [".",".","3",".",".",".",".",".","1"],[".",".",".",".",".","6",".",".","."],["1","7",".","4","3",".",".",".","."]],

    [["1",".",".",".",".","6",".","8","."],[".","6","4",".",".",".",".",".","."],[".",".",".",".","4",".",".",".","7"],
    [".",".",".",".","9",".","6",".","."],[".","7",".","4",".",".","5",".","."],["5",".",".",".","7",".","1",".","."],
    [".","5",".",".",".",".","3","2","."],["3",".",".",".",".","8",".",".","."],["4",".",".",".",".",".",".",".","."]],

    [[".",".",".","8",".",".",".",".","9"],[".","8","7","3",".",".",".","4","."],["6",".",".","7",".",".",".",".","."],
    [".",".","8","5",".",".","9","7","."],[".",".",".",".",".",".",".",".","."],[".","4","3",".",".","7","5",".","."],
    [".",".",".",".",".","3",".",".","."],[".","3",".",".",".","1","4","5","."],["4",".",".",".",".","2",".",".","1"]],

    [[".","4",".","5",".",".",".",".","."],["8",".",".",".","9",".",".","3","."],[".","7","6",".","2",".",".",".","."],
    [".","1","4","6",".",".",".",".","."],[".",".",".",".",".","9",".",".","7"],[".",".",".",".",".","3","6",".","."],
    [".",".","1",".",".","4",".","5","."],[".","6",".",".",".",".",".",".","3"],[".",".","7","1",".",".","2",".","."]]
]
