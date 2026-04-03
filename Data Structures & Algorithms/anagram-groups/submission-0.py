from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = []
        if len(strs) == 0:
            return ans
        else:
            a = [strs[0]]
            ans.append(a)
            strs.pop(0)
            for i in strs:
                temp = []
                for j in ans:
                    if Counter(i) == Counter(j[0]):
                        temp.append(i)
                        j+=temp
                if not temp:
                    temp.append(i)
                    ans.append(temp)
        return ans