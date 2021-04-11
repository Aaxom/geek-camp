# 双指针法
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        quick, slow = 1, 0
        while quick < len(nums):
            if nums[slow] != nums[quick]:
                if quick-slow>1:
                    nums[slow+1] = nums[quick]
                slow+=1
            quick+=1
        return slow+1


# 自己刚开始的垃圾解法
# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         tmp_char = None
#         for i in range(len(nums)):
#             if nums[i] == tmp_char:
#                 nums[i] = 'x'
#             else:
#                 tmp_char = nums[i]

#         while 'x' in nums:
#             nums.remove('x')

#         return len(nums)