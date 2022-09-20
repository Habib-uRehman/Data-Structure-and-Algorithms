# Brute Force Solution with n^2 complexity

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                pass
            elif nums[i] + nums[j] == target:
                return [i, j]


# Linear Solution.
def dic_sum(nums, target):
    dic = {}
    for i in range(len(nums)):
        curidx = nums[i]
        rem = target - curidx
        if rem in dic:
            return [i, dic[rem]]
        dic.update({curidx: i})


arr = [7, 2, 13, 11]
target = 24
print(dic_sum(arr, target))
