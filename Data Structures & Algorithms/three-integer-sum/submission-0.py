class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                temp = []
                if nums[left] + nums[right] == target:
                    temp+=[nums[left], nums[right], -(target)]
                    left+=1
                    right-=1
                    if temp not in ans:
                        ans.append(temp)
                elif nums[left] + nums[right] > target:
                    right-=1
                else:
                    left+=1
            
        return ans

