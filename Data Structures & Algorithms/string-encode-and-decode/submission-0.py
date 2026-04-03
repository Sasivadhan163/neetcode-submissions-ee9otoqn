class Solution:
    def __init__(self):
        self.lengths = []
    def encode(self, strs: List[str]) -> str:
        self.lengths = []
        s = ""
        for i in strs:
            self.lengths.append(len(i))
            s+=i
        return s
    def decode(self, s: str) -> List[str]:
        ans = []
        a = 0
        temp = ""
        for j in self.lengths:
            temp = s[a:a+j]
            ans.append(temp)
            a+=j
        return ans

