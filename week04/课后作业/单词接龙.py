# 我的辣鸡递归写法，就是DFS，LeetCode提交超时
class Solution:
    import math
    min_count = math.inf
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        steps = set()
        def only_one_diff(current, word):
            count = 0
            if len(current) == len(word):
                for i in range(len(word)):
                    if current[i] != word[i]:
                        count+=1
                return True if count==1 else False
            else:
                return False

        def dfs(current, end, wordList, steps, step_count):
            # 递归终止条件
            if current == end:
                self.min_count = min(self.min_count, step_count)
                return
            # 当层处理

            # 往下递归
            for word in wordList:
                if word not in steps and only_one_diff(current, word):
                    steps.add(word)
                    dfs(word, end, wordList, steps, step_count+1)
                    steps.remove(word)

        dfs(beginWord, endWord, wordList, steps, 0)
        return 0 if self.min_count == math.inf else self.min_count+1

# BFS的思路，最原始版本，也提交超时
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        visited = set()
        queue = []
        queue.append(beginWord)
        visited.add(beginWord)
        count = 0
        while queue:
            n = len(queue)
            count += 1
            for i in range(n):
                current = queue.pop(0)
                for word in wordList:
                    if word in visited: # 已经遍历过
                        continue
                    if not self.only_one_diff(current, word): # 不能转换的直接跳过
                        continue
                    if word == endWord: # 找到了solution
                        return count+1
                    visited.add(word)
                    queue.append(word)
        return 0
    def only_one_diff(self, current, word):
        count = 0
        if len(current) == len(word):
            for i in range(len(word)):
                if current[i] != word[i]:
                    count+=1
            return True if count==1 else False
        else:
            return False