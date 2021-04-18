# class Solution:
  # def generateParenthesis(self, n: int) -> None:
  #   # 先把问题想象成2n个格子里面，任意放“(”和“)”
  #   def _generate(level, s):
  #     # 递归边界
  #     if level >= 2*n:
  #       print(s)
  #       return
  #     # 当层处理：有两种情况，添加左括号或者右括号
  #     s1 = s+ '('
  #     s2 = s + ')'
  #     # 向下递归：两种情况分别向下递归
  #     _generate(level+1, s1)
  #     _generate(level+1, s2)

# class Solution:
#     results=[] # 尽量不要使用全局变量，LeetCode提交会有问题
#     def generateParenthesis(self, n: int) -> List:
#         def _generate(left, right, s):
#             # 递归边界
#             if left >= n and right >= n:
#                 self.results.append(s)
#                 return
#             # 当层处理和向下递归
#             # 括号合法的条件：左括号不超过n就可以加，右括号数不超过左括号就可以加
#             if left < n:
#                 s1 = s+ '('
#                 _generate(left+1, right, s1)
#             if right < left:
#                 s2 = s + ')'
#                 _generate(left, right+1, s2)

#         _generate(0,0, '')
#         return self.results
class Solution:
    def generateParenthesis(self, n: int) -> List:
        my_results=[]
        self.generate(0,0, n, '', my_results)
        return my_results
    def generate(self, left, right, n, s, my_results):
        # 递归边界
        if left >= n and right >= n:
            my_results.append(s)
            return
        # 当层处理和向下递归
        # 括号合法的条件：左括号不超过n就可以加，右括号数不超过左括号就可以加
        if left < n:
            s1 = s+ '('
            self.generate(left+1, right, n, s1, my_results)
        if right < left:
            s2 = s + ')'
            self.generate(left, right+1, n, s2, my_results)

if __name__ == '__main__':
  solution = Solution()
  solution.generateParenthesis(3)