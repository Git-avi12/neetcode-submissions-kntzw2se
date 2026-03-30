class TrieNode:
    def __init__(self):
        self.children = {}
        self.EOW = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if not i in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.EOW = True

    def search(self, word: str) -> bool:
        def dfs(j,root):
            node = root
            for i in range(j,len(word)):
                c = word[i]
                if c==".":
                    for child in node.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.EOW
        return dfs(0,self.root)

        
        
