from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_k = {}
        for i in nums:
            if i in hash_k:
                hash_k[i] +=1
            else:
                hash_k[i] = 1

        list_counter = []
            
        for i in hash_k:
            list_counter.append([i, hash_k[i]])
        
        list_counter.sort(key = lambda x:x[1])
        print(list_counter)
        return [i[0] for i in list_counter[-k:]]

if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k))
'''
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

Test case passed
'''