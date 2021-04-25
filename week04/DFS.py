# 递归写法
visited = set()
def dfs_recursive(node, visited):
  # 递归终止条件
  if node in visited:
    return
  # 当层处理
  visited.add(node)
  # 向下递归
  for next_node in visited.children():
    if next_node not in visited:
      dfs_recursive(next_node, visited)


# 非递归写法
def dfs_non_recursive(self, tree):
  if tree.root is None:
    return []

  visited, stack = [], [tree.root]

  while stack:
    node = stack.pop()
    visited.add(node)

    process(node)
    nodes = generate_related_nodes(node)
    stack.push(nodes)

