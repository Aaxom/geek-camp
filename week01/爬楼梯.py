# 1. 暴力递归
class Solution:
    def climbStairs(self, n: int) -> int:
        # 递归边界条件，当只有0或1级台阶时，只有一种爬法
        if n==0 or n==1:
            return 1

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
        for i in range(len(results)):
            if i == 0 or i == 1:
                results[i] == 1
            else:
                results[i] = results[i-1] + results[i-2]

        return results[-1]

# 4. 变量优化
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(2, n+1):
            a, b = b, a+b
        return b


# 5. 斐波那契公式法
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt_5 = math.sqrt(5)
        fib_n = math.pow((1+sqrt_5)/2, n+1) - math.pow((1-sqrt_5)/2, n+1)
        return int(fib_n / sqrt_5)

