
arr = [1, 5, 33, 5, 1, 7, 3, 8, 2]


def merge(s1, s2, arr):
    i = 0
    j = 0
    x = 0
    while i < len(s1) and j < len(s2):
        if s1[i] < s2[j]:
            arr[x] = s1[i]
            x += 1
            i += 1
        else:
            arr[x] = s2[j]
            x += 1
            j += 1
    while i < len(s1):
        arr[x] = s1[i]
        x += 1
        i += 1
    while j < len(s2):
        arr[x] = s2[j]
        x += 1
        j += 1
    return arr


def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return
    mid = len(arr) // 2
    s1 = arr[0:mid]
    s2 = arr[mid:]
    merge_sort(s1)
    merge_sort(s2)
    return merge(s1, s2, arr)


print(merge_sort(arr))