class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        has={"(":")","[":"]","{":"}"}
        for i in s:
            if i in has:
                stk.append(i)
            else:
                if stk:
                    if i==has.get(stk[-1],0):
                        print(i)
                        stk.pop()
                    else:
                        return False
                else:
                    return False
        if stk:
            return False
        return True