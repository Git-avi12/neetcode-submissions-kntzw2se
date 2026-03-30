class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        has={"(":")","[":"]","{":"}"}
        for i in s:
            if i in has:
                stk.append(i)
            else:
                if stk and i==has.get(stk[-1],0):
                    stk.pop()
                else:
                    return False
        if stk:
            return False
        return True