class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        i = len(nums)-1
        while i>=0 and not ans:
            diff = target - nums[i]
            if diff in nums and nums.index(diff)!=i:
                ans.append(nums.index(diff))
                ans.append(i)
            else:
                i-=1
        return ans
