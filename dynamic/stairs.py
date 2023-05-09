# QUESTION: if you can walk 1 or 2 steps, how many ways can you walk up stairs of n length to exactly the top?


# n = 0 => 0
# n = 1 => [1] = 1
# n = 2 => [1, 1], [2] = 2
# n = 3 => [1, 1, 1], [1, 2], [2, 1] = 3
# n = 4 => [1, 1, 1, 1], [1, 1, 2], [2, 1, 1], [1, 2, 1], [2, 2] = 5
# n = 5 => [1, 1, 1, 1, 1], [1, 1, 1, 2], [2, 1, 1, 1], [1, 1, 2, 1], [1, 2, 1, 1],[2, 2, 1] ... = 8
# n = 6 => 13
# n = 7 => 21
# n = 8 => 34
# n = 9 => 55

# n stairs = (n - 1 stairs) + (n - 2 stairs) # n-1 + n-2 create the n options

# ANSWER:
# stairs is the recursion of fibonacci + 1


def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def stairways(n):
    return fib(n + 1)

answers = []
for t in range(10):
    answers.append(stairways(t))

print(answers)