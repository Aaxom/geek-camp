# 递归结题函数结构
# def recursive(level, param1, param2, ...):
#     # 递归结束条件、边界条件
#     if level > MAX_LEVEL:
#         process_result
#         return
#     # 本层处理操作
#     process(level, data...)
#     # 往下递归
#     self.recursive(level+1, p1...)
#     # 递归后清理、还原操作


# 1. 暴力递归
class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归边界条件，当只有0或1级台阶时，只有一种爬法
        if n==0 or n==1:
            return 1
        # 当n>1时，终止条件也可以用下面这种
        # if n==1:
        #     return 1
        # elif n==2:
        #     return 2

        # 爬n级台阶的方法数 = 爬n-1级台阶的方法数（这次走1步） + 爬n-2级台阶的方法数（这次走2步）
        return self.climbStairs(n-1) + self.climbStairs(n-2)


# 2. 记忆性递归
class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(i: int, results: List):
            # 递归边界条件，当只有0或1级台阶时，只有一种爬法
            if i==0 or i==1:
                return 1

            if results[i]==-1:
                results[i] = dfs(i-1, results) + dfs(i-2, results)
            # 爬n级台阶的方法数 = 爬n-1级台阶的方法数（这次走1步） + 爬n-2级台阶的方法数（这次走2步）
            return results[i]
        

        return (dfs(n, [-1]*(n+1)))


# 3. 动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        results = [1]*(n+1)
        for i in range(n+1): # 初始值为1情况下，可以缩短遍历范围，用range(2, n+1)
            # 下面可以省略，因为初始化默认就是1
            # if n==0 or n==1:
            #     results[i] = 1
            if i>1:
                results[i] = results[i-1]+results[i-2]
        # return results[-1]
        return results[n]

# 4. 动态规划（变量优化）
class Solution:
    def climbStairs(self, n: int) -> int:
        front, back = 1, 1
        for i in range(2, n+1):
            front, back = back, front + back
        return back


# 5. 斐波那契公式法
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt_5 = math.sqrt(5)
        fib_n = math.pow((1+sqrt_5)/2, n+1) - math.pow((1-sqrt_5)/2, n+1)
        return int(fib_n / sqrt_5)

