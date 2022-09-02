def permute(k, A, B):
    a_dash = sorted(A, reverse= True)
    b_dash = sorted(B)
    i = 0
    res = ''
    while i < len(A):
        if a_dash[i] + b_dash[i] < k:
            res = 'NO'
            return res
        else:
            res = 'YES'
        i += 1
    return res

a = [1,3]
b = [3,1]
k = 4
print(permute(k, a, b))
