# given string sequence, find longest palindrome substring within and return it
import numpy as np

def LPS(seq: str) -> str:
    # DYNAMIC PROGRAMMING

    # for all i,j in seq
    # @ seq[i][j]
    # if they are the same, seq[i][j] =  seq[i+1][j-1] + 2
    # else max(seq[i][j-1], seq[i+1][j]
    res = np.zeros(shape=(len(seq), len(seq)))
    for k in range(0, len(seq)):
        res[k][k] = 1


    for i in range(2, len(seq) + 1):
        j = 0
        while j < (len(seq) - i + 1) :
            d = j + i - 1
            if seq[j] == seq[d] and i == 2:
                res[j][d] = 2
            if seq[j] == seq[d]:
                res[j][d] = res[j+1][d-1] + 2
            else:
                res[j][d] = max(res[j][d-1], res[j+1][d])
            j = j+1

    print(res)
    return res[0][len(seq)-1]

print(LPS("BABCBAB"))
print(LPS("BABC"))
print(LPS("BBC"))
print(LPS("CBBBBC"))
print(LPS("CBBCCBBC")) # WRONG!
print(LPS("CBBCCDDBBC")) # WRONG!