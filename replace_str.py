def replace_str(s, a, b):
    if len(s) == 0:
        return s
    smaller = replace_str(s[1:], a, b)
    if s[0] == a:
        return b + smaller
    else:
        return s[0] + smaller


st = 'axax'
print(replace_str(st, 'a', 'z'))
