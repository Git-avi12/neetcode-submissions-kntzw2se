class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for i in s:
            if i.isalnum():
                l.append(i.lower())
        l.reverse()
        inv_l = l.copy()
        l.reverse()
        print(l)
        print(inv_l)

        if inv_l == l:
            return True
        else:
            return False
