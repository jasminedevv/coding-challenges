"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# get index 1

# get index 2

def twoSum(nums, target):
    """
    O(n2) Solution
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums.sort()
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if num1 + num2 == target:
                return i, j
    raise KeyError("No two numbers in this list add up to", target)
        
            
array = [10, 2, 7, 11, 15]

print(twoSum(array, 26))