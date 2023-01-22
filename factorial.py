# Recursion is when a function call itself.
# In mathmatics we call it PMI, proving mathematical induction.
# PMI states that you have to prove a function that it is true. For example if f(n) is true you have to prove it.
# To prove a function is true you have to prove two tasks.
# Task 1: f(0) is true. i,e f(n) = n. we can say that f(n) = n * (n+1) / 2
# Assume that f(k) is true.
# Task 2: f(k+1) is also true. hence it will be true for all f(n)

# Find the factorial of a number using recursion
def fact(n):
    # define a base case or else it will keep running.
    if n == 0:
        return 1
    # Formula of factorial is f(n) = n * (n-1)!
    return n * fact(n - 1)


print(fact(6))
