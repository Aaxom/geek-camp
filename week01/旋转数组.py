# 思路：https://leetcode-cn.com/problems/rotate-array/solution/shu-zu-fan-zhuan-xuan-zhuan-shu-zu-by-de-5937/
# 首先对整个数组实行翻转，这样子原数组中需要翻转的子数组，就会跑到数组最前面。
# 这时候，从k处分隔数组，左右两数组，各自进行翻转即可。
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:k], nums[k:] = nums[::-1][:k][::-1], nums[::-1][k:][::-1]