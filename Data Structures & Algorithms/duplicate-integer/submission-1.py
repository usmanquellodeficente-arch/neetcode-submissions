class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        not_duplicate = set(nums)
        return  not len(not_duplicate) == len(nums)