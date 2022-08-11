# Recursion is when a function call itself.
# In mathmatics we call it PMI, proving mathematical induction.
# PMI states that you have to prove a function that it is true. For example if f(n) is true you have to prove it.
# To prove a function is true you have to prove two tasks.
# Task 1: f(0) is true. i,e f(n) = n. we can say that f(n) = n * (n+1) / 2
# Assume that f(k) is true.
# Task 2: f(k+1) is also true. hence it will be true for all f(n)


# Check if list is sorted or not using recursion.
arr = [10, 2, 5, 6]


def is_sorted(n):
    l = len(n)
    if l == 0 or l == 1:
        return True
    if n[0] > n[1]:
        return False
    smaller_list = n[1:]
    return is_sorted(smaller_list)


# A little better solution
def is_sort_better(n, si):
    l = len(n)
    if si == l - 1 or si == l:
        return True
    if n[si] > n[si + 1]:
        return False
    return is_sort_better(n, si + 1)


print(is_sort_better(arr, 1))
