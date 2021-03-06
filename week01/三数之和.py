# 3数之和

# 总体可以转化为2数之和的思维来做
# a+b+c=0 => a+b=-c


# 方法一：3重暴力求解
# 1. 创建一个set存放最终结果，自动去重
# 2. 第一重循环：下标i从0到len-2
# 3. 第二重循环：下标j从i+1到len-1
# 4. 第三重循环：下标k从j+1到len-2
# 5. 判断 nums[i]+nums[j]+nums[k]==0 就是a+b+c==0
# 6. 如果成立，则找到一个解，[nums[i], nums[j], nums[k]]三个数之间先排序后，加入结果集set



# 方法二：2重暴力+哈希
# 1. 创建一个set存放最终结果，自动去重
# 2. 设下标i从0到len-1遍历数组，nums[i]作为此次的c
# 3. 准备一个hashmap
# 4. 设下标j从i+1到len，二重循环数组
# 5. 计算-c减去nums[j]是否存在于hashmap中，
# 6. 不存在就把nums[j]加进去，存在的话就是找到了一组3结果，就把3个数添加到结果set中



# 方法三：夹逼（双指针）
1. 将数组排序，设有排序后数组：-4, -1, -1, -1, 0, 1, 2
2. 令target指向第一位开始遍历（-4），i指向target+1位开始遍历（刚开始是第二位，是-1），j指向末位（2），
3. 比较 -nums[target] 和 nums[i]+ nums[j]：
4. 如果前者>后者，则i++，如果前者<后者，j--，如果相等就是找到一组解
