class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = list(set(nums))
        return len(a) != len(nums)
