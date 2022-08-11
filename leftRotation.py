
# Hacker rank problem. Called LeftRotation, 2 solutions. one with slower version and one with fast
def swap(d, arr):
    # for i in range(d):
    #     new_arr = []
    #     for x in range(len(arr) - 1):
    #         new_arr.append(arr[x + 1])
    #     new_arr.append(arr[0])
    #     arr = new_arr
    #
    # return new_arr
    new_arr = []
    for value in (arr[d:] + arr[0:d]):
        new_arr.append(value)
    return new_arr

arr = [1, 2, 3, 4, 5]
print(swap(2,arr))