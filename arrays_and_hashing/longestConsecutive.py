from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        temp_length = 0
        k = set(nums)
        for i in nums:
            if i-1 not in k:
                temp_length = 1
                temp = i
                while temp + 1 in k:
                    # temp_list.append(temp + 1)
                    temp = temp + 1
                    temp_length += 1
                longest = max(temp_length, longest)

                # if len(master_list) < len(temp_list):
                    # master_list = temp_list
        return longest


if __name__ == "__main__":
    '''
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

 

    Example 1:

    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
    Example 2:

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
    '''
    Sol = Solution()
    nums = [100,4,200,1,3,2]
    print(Sol.longestConsecutive(nums))
    nums = [0,3,7,2,5,8,4,6,0,1]
    print(Sol.longestConsecutive(nums))

