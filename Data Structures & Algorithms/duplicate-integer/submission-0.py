class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nset = set()
        for i in range(len(nums)):
            if nums[i] in nset:
                return True
            nset.add(nums[i])
        return False