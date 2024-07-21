from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        while l<r:
            if numbers[r] + numbers[l] > target:
                r-=1
            elif numbers[r] + numbers[l] < target:
                l+=1
            else:
                return [l+1,r+1]
            
if __name__ == '__main__':
    '''
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
    '''
    
    numbers = [2,7,11,15]
    target = 9

    sol = Solution()
    print(sol.twoSum(numbers, target))