class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        def _insert(word):
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word
        
        for w in words:
            _insert(w)
        
        row, col = len(board), len(board[0])
        path = set()
        res = set()

        def dfs(r, c, node):
            if (r < 0) or (r >=row) or (c<0) or (c>= col) or ((r,c) in path) or (board[r][c] not in node.children):
                return False
            node = node.children[board[r][c]]
            if node.word != None:
                res.add(node.word)
            path.add((r,c))

           
            dfs(r-1, c, node) 
            dfs(r+1, c, node)
            dfs(r, c-1, node)
            dfs(r, c+1, node)
            

            path.remove((r,c))

            
        
        for r in range(row):
            for c in range(col):
                dfs(r, c, root)
        return list(res)

            
            
