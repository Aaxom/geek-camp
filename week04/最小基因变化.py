# 暴力法，没有做完
# 1. 遍历基因库bank，找到和start只差一个碱基的基因
# 2. 标记该基因库的基因，表示已经变换过，并赋值给current
# 3. 遍历基因库bank剩余基因，找到和current只差一个碱基的基因

# class Solution:
#     def minMutation(self, start: str, end: str, bank: List[str]) -> int:
#         import copy
#         min_level = -1

#         def only_one_diff(current, gene):
#             count = 0
#             if len(current) == len(gene):
#                 for i in range(len(gene)):
#                     if current[i] != gene[i]:
#                         count+=1
#                 return True if count==1 else False
#             else:
#                 return False

#         def get_gene_change_count(current, level, available_genes):
#             print("新一层的available_genes: "+str(available_genes))
#             # 递归终止
#             if current == end:
#                 return level
#             if not available_genes:
#                 return -1

#             for gene in available_genes:
#                 print("对比current和当前遍历的gene: "+current+"\t"+gene)
#                 if only_one_diff(current, gene):
#                     print("替换成: "+gene)
#                     new_available_genes = copy.copy(available_genes)
#                     new_available_genes.remove(gene)
#                     # current变成gene向下递归
#                     new_level = get_gene_change_count(gene, level+1, new_available_genes)
#                     if new_level and new_level!=-1:
#                         new_level = min(new_level, min_level)
#                         return new_level
#             return -1

#         return get_gene_change_count(start, 0, bank)


class Solution:
    import math
    min_count = math.inf
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def only_one_diff(current, gene):
            count = 0
            if len(current) == len(gene):
                for i in range(len(gene)):
                    if current[i] != gene[i]:
                        count+=1
                return True if count==1 else False
            else:
                return False

        def dfs(step, step_count, current, end, bank):
            # 递归终止条件
            if current == end:
                self.min_count = min(self.min_count, step_count)
                return
            # 进入下一层递归
            for gene in bank:
                if only_one_diff(current, gene) and gene not in step:
                    # print("进入下一层递归，step_count: "+str(step_count)+"  gene:"+gene)
                    step.add(gene)
                    dfs(step, step_count+1, gene, end, bank)
                    step.remove(gene)

        dfs(set(), 0, start, end, bank)
        return -1 if self.min_count == math.inf else self.min_count