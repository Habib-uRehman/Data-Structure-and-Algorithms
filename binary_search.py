def binary_search(arr, x, si, ei):
    if si > ei:
        return -1
    mid = (si + ei) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] < x:  # [1,2,3,4,5,6,7]
        return binary_search(arr, x, mid + 1, ei)
    else:
        return binary_search(arr, x, si, mid - 1)


ls = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(ls, 8, 0, 6))
