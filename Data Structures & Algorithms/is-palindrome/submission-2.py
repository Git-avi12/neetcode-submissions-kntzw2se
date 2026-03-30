class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=[]
        for i in s:
            if i.isalnum():
                st.append(i.lower())
        if "".join(st)=="".join(st[::-1]):
            return True
        return False

