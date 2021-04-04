class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left, right = 0, 0
        for i in range(nums):
            if i != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1






        # #尝试方法3
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         pass
        #     else:
        #         mark = i
        #         for j in range(-len(nums)+i-1,-len(nums)-1,-1):
        #             #原来的nums[i]也就是nums[-len+i]，那么j应该是range(-len+i-1,-len-1,-1)
        #             #range取值需要想清楚
        #             if nums[j] == 0:
        #                 mark = j
        #             else:
        #                 break
        #         if mark != i:
        #             nums[mark], nums[i] = nums[i], 0





# 1. （此题不允许）新建一个同样长度的全0数组2，遍历数组1，遇到非零就填充到数组2
# 2. 遍历数组，遇到0就删除，同时末尾补上0
# 3. 遍历数组，遇到0就继续向后看，遇到非0就往前看是否为0，是的话就前移，只要往前看时候遇到一个非0，就不用再看了
# 4. 遍历删除所有0，然后补充到后面