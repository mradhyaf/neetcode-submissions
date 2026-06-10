class Solution:
    def rob(self, nums: List[int]) -> int:
        no_take = 0
        take = nums[0]

        for i in range(1, len(nums)):
            n_no_take = max(no_take, take)
            n_take = no_take + nums[i]

            no_take = n_no_take
            take = n_take

        return max(no_take, take)
