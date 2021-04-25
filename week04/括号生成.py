class Solution:
    def generateParenthesis(self, n: int) -> List:
        results = []
        self.generate(0, 0, n, "", results)
        return results

    def generate(self, left, right, n, s, results):
        # 递归终止条件
        if left>=n and right>=n:
            results.append(s)
            return
        
        if left < n:
            s1 = s + "("
            self.generate(left+1, right, n, s1, results)
        if right < left:
            s2 = s + ")"
            self.generate(left, right+1, n, s2, results)

# n对括号就是2n个格子
# 先进行简单的排列组合，不关注括号的合法性，有2^(2n)种
# 递归终止条件：左括号和右括号数量都>=n

# 检查括号合法性
# 如果左括号数量 < n，可以继续加左括号进行下一层递归
# 如果右括号数量 < 左括号数量，可以继续加右括号进行下一层递归
