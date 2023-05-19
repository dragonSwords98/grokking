# Contributed by: Bryan Ling


# 7.3 Write a function which takes as input a phone number, specified
# as a string of digits, return all possible character sequences that correspond to the phone
# number. The cell phone keypad is specified by a mapping M that takes a digit and returns
# the corresponding set of characters. The character sequences do not have to be legal words or
# phrases.

M = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]



# Given a sequence of digits in string form, find all possible character combinations
def mnemonics(sequence: str):

    # Given phone digits, yield corresponding letters for each digit
    sequence_in_M = map((lambda m : M[int(m)]), sequence)

    iter_on_M = iter(sequence_in_M)
    for I in sequence_in_M:
        mnemonics_helper(I, next(iter_on_M))


def mnemonics_helper(I, J):
    res = []
    for i in I:
        findAllCombos(i, J)
    return res

def findAllCombos(i, J):
    res = []
    for j in J:
        res.append(i + j)
    return res

