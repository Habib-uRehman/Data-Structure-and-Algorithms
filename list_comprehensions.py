# List Comprehensions HR
x = 2
y = 3
z = 4
n = 3

# With out List comprehensions
# res = []
# for i in range(a+1):
#     for j in range(b+1):
#         for x in range(z+1):
#             ls = []
#             ls.append(i)
#             ls.append(j)
#             ls.append(x)
#             if sum(ls) == n:
#                 pass
#             else:
#                 res.append(ls)
# print(res)

# Using list comprehensions
res = [[q, j, i] for q in range(x) for j in range(y) for i in range(z) if not i + j + q == n]
print(res)