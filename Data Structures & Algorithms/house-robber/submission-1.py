class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        tab = [[0, 0] for i in range(n)]
        tab[0][1] = nums[0]

        for i in range(1, n):
            tab[i][0] = max(tab[i-1][0], tab[i-1][1])
            tab[i][1] = tab[i-1][0] + nums[i]

        return max(tab[n-1][0], tab[n-1][1])
