# Recursion is when a function call itself.
# In mathmatics we call it PMI, proving mathematical induction.
# PMI states that you have to prove a function that it is true. For example if f(n) is true you have to prove it.
# To prove a function is true you have to prove two tasks.
# Task 1: f(0) is true. i,e f(n) = n. we can say that f(n) = n * (n+1) / 2
# Assume that f(k) is true.
# Task 2: f(k+1) is also true. hence it will be true for all f(n)


def last_index(arr, x):
    if len(arr) == 0:
        return -1
    small_list = arr[1:]
    output = last_index(small_list, x)
    if output != -1:
        return output + 1
    else:
        if arr[0] == x:
            return 0
        else:
            return -1


def last_index_position(arr, x, ai):
    if ai == len(arr):
        return -1
    small_list = last_index_position(arr, x, ai + 1)
    if small_list != -1:
        return small_list
    else:
        if arr[ai] == x:
            return ai
        else:
            return -1


ls = [1, 66, 3, 66, 1, 8, 66]
print(last_index_position(ls, 66, 0))
