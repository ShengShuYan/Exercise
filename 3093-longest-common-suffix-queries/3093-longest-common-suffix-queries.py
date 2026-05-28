class TrieNode:
    def __init__(self):
        self.children = {}
        # 记录经过该节点的所有字符串中，长度最短且索引最小的字符串下标
        self.best_idx = -1 

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        # 辅助函数：判断 idx1 对应的字符串是否比 idx2 更优
        def is_better(idx1, idx2):
            if idx2 == -1: return True
            len1 = len(wordsContainer[idx1])
            len2 = len(wordsContainer[idx2])
            if len1 != len2:
                return len1 < len2
            return idx1 < idx2

        # 1. 寻找全局最优解（给根节点和完全不匹配的情况备用）
        best_overall_idx = 0
        for i in range(1, len(wordsContainer)):
            if is_better(i, best_overall_idx):
                best_overall_idx = i
        root.best_idx = best_overall_idx
        
        # 2. 构建字典树 (插入翻转后的字符串)
        for i, word in enumerate(wordsContainer):
            curr = root
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                # 更新当前节点的最优索引
                if is_better(i, curr.best_idx):
                    curr.best_idx = i
                    
        # 3. 处理每个查询
        ans = []
        for query in wordsQuery:
            curr = root
            for char in reversed(query):
                # 如果匹配上了，就继续往下走
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    # 匹配不上了，就停在当前前缀能达到的最深节点
                    break
            ans.append(curr.best_idx)
            
        return ans