class Solution:
  # 前序知识：
  # 如果 x-y=k ，可以判断(x, y)点在 y=x-k 函数线上 => 撇、丿
  # 如果 x+y=k ，可以判断(x, y)点在 y=-x+k 函数线上 => 捺
  # 根据上面的知识，可以知道，通过判断x-y是否等于某个数k，就可以判断它在不在某条撇线上；同理用x+y可以判断一个点是否在捺线上
  def solveNQueens(self, n: int) -> List[List[str]]:
    def dfs(queens, pie, na):
      """
      queens存放已经有的皇后所在的列，y不在queens表示不在皇后的竖直攻击范围内
      pie存放包含撇线的偏移量k，包含了一条撇线的特征，x-y不在pie中，就表示不在皇后的撇线攻击范围内
      na存放包含撇线的负偏移量-k，包含了一条捺线的特征，x+y不在pie中，就表示不在皇后的捺线攻击范围内
      """
      p = len(queens)
      # 递归终止条件
      if p == n:
        result.append(queens)
        return None
      # 当层处理

      # 向下递归
      for q in range(n):
        # 因为q是从0到n的，所以q每次循环都不同，新皇后不会出现在原有皇后的横向攻击范围内
        # 所有if判断不用判断q
        if (q not in queens) and (p-q not in pie) and (p+q not in na):
          dfs(queens+[q], pie+[p-q], na+[p+q])

    result = []
    dfs([], [], [])
    
    return [["."*i + "Q" + "."*(n-i-1) for i in col] for col in result]


