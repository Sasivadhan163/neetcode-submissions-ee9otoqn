class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = []
        prefix = []
        suffix = []
        for i in range(len(nums)-1):
            temp = 1
            for j in range(i+1,len(nums)):
                temp*=nums[j]
            suffix.append(temp)
        suffix.append(1)
        
        for i in range(0, len(nums)):
            temp = 1
            for j in range(i):
                temp*=nums[j]
            prefix.append(temp)
        
        for i in range(len(nums)):
            ans.append(prefix[i]*suffix[i])
        
        return ans

