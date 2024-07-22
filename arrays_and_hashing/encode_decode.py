from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        en = ""
        for i in strs:
            ln = len(i)
            en+= f"#{ln}{i}"
        print(en)
        return en
            


    def decode(self, s: str) -> List[str]:
        temp = []
        master = []
        start_flag = 0
        len_to_check = -1
        idx = 0
        str_ = ""
        while idx < len(s):
            print(s[idx])
            if s[idx] == "#" or look_for==0:
                master.append(str_)
                look_for = len(s[idx+1])
                idx+=1
                str_ = ""
                print(master)
                continue
            idx+=1
            look_for-=1
            if idx != len(s):
                
                str_+=s[idx]

            
            
        return master
            
        
if __name__ == '__main__':
    sol = Solution()
    inp = ["neet","code","love","you"]

    en = sol.encode(inp)
    out = sol.decode(en)
    print(out)