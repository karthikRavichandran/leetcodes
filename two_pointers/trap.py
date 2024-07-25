from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_arr = []
        right_arr = []
        h = 0
        for i in height:
            left_arr.append(h)
            if h<i:
                h=i
        h=0

        for i in range(len(height)-1,-1,-1):
            right_arr.append(h)
            if h<height[i]:
                h=height[i]
        right_arr = right_arr[::-1]

        sum_t = 0
        for i in range(len(height)):
            k = max(min(right_arr[i], left_arr[i]) - height[i], 0)
            sum_t +=k
        return sum_t

if __name__ == '__main__':
    '''
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

    Example 1:


    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
    Example 2:

    Input: height = [4,2,0,3,2,5]
    Output: 9

    '''
    height = [4,2,0,3,2,5]
    sol = Solution()
    print(sol.trap(height))
