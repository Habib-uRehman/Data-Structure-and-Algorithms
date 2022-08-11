# Recursion is when a function call itself.
# In mathmatics we call it PMI, proving mathematical induction.
# PMI states that you have to prove a function that it is true. For example if f(n) is true you have to prove it.
# To prove a function is true you have to prove two tasks.
# Task 1: f(0) is true. i,e f(n) = n. we can say that f(n) = n * (n+1) / 2
# Assume that f(k) is true.
# Task 2: f(k+1) is also true. hence it will be true for all f(n)


def first_index(ls, x):
    count = 0
    if len(ls) == 0:
        return -1
    if ls[0] == x:
        return count
    count += 1
    smaller_ls = ls[1:]
    result = first_index(smaller_ls, x)
    if result == -1:
        return -1
    else:
        return result + 1


# Solution 2.

def first_index_better(ls, x, li):
    if len(ls) == 1:
        return -1
    if ls[li] == x:
        return li
    smaller_ls = first_index_better(ls, x, li + 1)
    return smaller_ls


arr = [5, 6, 88, 2, 11]
print(first_index_better(arr, 88, 0))
print(first_index(arr, 88))