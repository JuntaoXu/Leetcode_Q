class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    ans += 1
        return ans