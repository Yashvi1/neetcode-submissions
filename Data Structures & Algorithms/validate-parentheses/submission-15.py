class Solution:
    
    def isValid(self, s: str) -> bool:
        pair = {
        "{":"}",
        "(":")",
        "[":"]"
        }

        open = ["(", "[", "{"]
        close = [")","]","}"]

        bracket = []
        if len(s) <= 1:
            return False
        for b in s:
            if b in open:
                bracket.append(b)
            elif b in close:
                if not bracket:
                    return False
                if pair[bracket[-1]] != b:
                    return False
                else:
                    bracket.pop()
        if len(bracket) > 0:
            return False
        return True
            


        