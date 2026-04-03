class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums.sort()
        a = list(set(nums))
        b = []
        for i in a:
            b.append(nums.count(i))
        
        ans = []
        for i in range(k):
            temp = b.index(max(b))
            num = a[temp]
            ans.append(num)
            a.remove(num)
            b.pop(temp)
        return ans
    
