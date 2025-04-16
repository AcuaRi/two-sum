from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    #MY ANSWER
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
    inputList = input('Input: nums = ')
    inputTarget = int(input('Input: target = '))

    twoSum(nums=inputList, target=inputTarget)