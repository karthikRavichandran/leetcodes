class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hs = {}
        for idx, i in enumerate(arr):
            if i not in hs:
                hs[i] = idx
            else:
                hs[i] = -1
        p = list(set(hs.values()))
        print(p)
        if k-1 >= len(p):
            return ""
        elif p[k-1] <0:
            return ""
        else:
            return arr[p[k-1]]
        # print(p[k-1]) 
#https://leetcode.com/problems/kth-distinct-string-in-an-array/?envType=daily-question&envId=2024-08-05
        



        
