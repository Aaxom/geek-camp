class Solution:
    def trap(self, height: List[int]) -> int:
        if (height==None):
            return 0
        stack = []
        ans = 0
        for i in range(len(height)):
            while(len(stack)!=0 and (height[stack[-1]] < height[i])):
                current = stack.pop()

                # 遇到一排相同高度的柱子
                while(len(stack)!=0 and height[stack[-1]] == height[current]):
                    stack.pop()

                if len(stack)!=0:
                    # stack_top是左边界柱子的高度
                    stack_top = stack[-1]
                    # 计算水的面积：(MIN(左边界柱子高度，右边界柱子高度) - 该层水的底高) * 两个柱子距离
                    # 就是 (min(stack_top, height[i]) - height[current]) * (i-stack_top-1)
                    ans += (min(height[stack_top], height[i]) - height[current]) * (i - stack_top - 1)
            
            stack.append(i)
        return ans





# 使用栈求解

# 初始化栈[]
# 从左往右遍历
# while循环，当栈空时候就入栈；非空时，如果遇到新的柱子height[i] > 栈顶柱(左边柱)高度，就出栈
# 继续判断如果出栈后的栈顶柱子高度 == 刚刚出栈的柱子高度，就是遇到了一排等高的底盘，持续出栈
# 出栈到最后，栈还没有空，也就是水并没从左边界溢出，此时的取得真正的最左边柱stack_top，
# 开始计算水の面积重点！！！(MIN(左边界柱子高度，右边界柱子高度) - 该层水的底高) * 两个柱子距离
# 就是 (min(stack_top, height[i]) - height[current]) * (i-stack_top-1)
# 检查循环跳出条件