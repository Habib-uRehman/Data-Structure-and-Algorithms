def partition(a, si, ei):
    p = a[si]
    i = 0
    for y in range(si, ei + 1):
        if a[y] < p:
            i += 1

    a[si + i], a[si] = a[si], a[si + i]
    p = si + i
    x = si
    j = ei
    while i < j:
        if a[x] < p:
            x += 1
        elif a[j] >= p:
            j -= 1
        else:
            temp = a[j]
            a[j] = a[x]
            a[x] = temp
            i = i + 1
            j = j - 1
    return p


def quick_sort(a, si, ei):
    if si > ei:
        return
    p = partition(a, si, ei)
    quick_sort(a, si, p - 1)
    quick_sort(a, p + 1, ei)


arr = [61,4,11, 1, 5, 7]
quick_sort(arr, 0, len(arr) - 1)
print(arr)