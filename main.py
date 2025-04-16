from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    #MY ANSWER
    print(f"Input: nums = {nums}, target = {target}")
    i = 0
    while i < (len(nums)-1):
        j = i+1
        while j < len(nums):
            if nums[i] + nums[j] == target:
                print(f"Output: [{i},{j}]")
            j+=1
        i+=1

    return

if __name__ == '__main__':
    twoSum([2,7,11,15], 9)
    twoSum([3,2,4], 6)
    twoSum([3,3], 6)