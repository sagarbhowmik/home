"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

nums = [3, 3], target = 6, return [0, 1]

nums = [3, 2, 4], target = 6, return [1, 2]
"""

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        print("Numbers entered are: {}".format(nums))
        print("Target is: {}".format(target))
        nums_dict = {key:value for key, value in enumerate(nums)}
        print(nums_dict)
        indices = []
        for key in nums_dict:
            print("{}: {}".format(key, nums_dict[key]))
            next_num = target - nums_dict[key]
            if next_num in nums_dict.values():
                new_key = [k for k,v in nums_dict.items() if v == next_num and k != key]
                if new_key:
                    indices.append(key)
                    indices.append(new_key[0])
                    return indices


def main():
        sol = Solution()
        indices = sol.twoSum([3, 2, 4], 6)
        if not indices:
            print("none of the combination of two integers' sum is equal to target")
        else:
            print(indices)


if __name__ == "__main__":
        main()
