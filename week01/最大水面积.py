class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, area = 0, len(height)-1, 0
        while(i<j):
            area = max(area, (j-i) * min(height[i], height[j]))
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return area



#计算水面积的方法
#min(Ai1,Ai2)*|i1-i2|

# 方法一，暴力穷举，左边遍历0-(len-2),右边遍历1-(len-1)

# 方法二，双指针法
#设i<j
#MIN(height[i], height[j]) * (j-i) 的最大值
#1. 先i指向0，j指向末尾len-1
#2. 初始化最大面积area_result = 0
#3. 开始循环，i<j为进入循环的条件
#4. 目前面积area = MIN(height[i], height[j]) * (j-i)
#5. 如果height[i] < height[j]，i向右移动，j不移动；如果height[i] > height[j]，i不移动，j向左移动
#6. 求面积，如果area大于原来的area_result，就修改area_result
#7. 循环退出时，area_result最大

#第5步详解：经过一次对比后，可以确认哪边是短板。这时候要确定如何移动，无论如何移动，都是宽度变窄，如果短板向内移动，短板可能变长，水会变高，一变高+一变短，面积还有机会变大，如果长边向内移动，水位一直和短板一样不会变化，但水宽变短，总的来看，水的面积只会变小，所以应该移动短板。