class TrieNode:
    def __init__(self):
        self.child={}
        self.EOW = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.child:
                cur.child[i] = TrieNode()
            cur=cur.child[i]
        cur.EOW = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                c = word[i]
                if c==".":
                    for child in cur.child.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in cur.child:
                        return False
                    cur = cur.child[c]
            return cur.EOW
        return dfs(0,self.root)
        
