class Solution:
    
    def isValid(self, s: str) -> bool:
        pair = {
        "{":"}",
        "(":")",
        "[":"]"
        }

        open = ["(", "[", "{"]

        bracket = []
        for b in s:
            if b in open:
                bracket.append(b)
            elif b not in open:
                if not bracket:
                    return False
                if pair[bracket[-1]] != b:
                    return False
                else:
                    bracket.pop()
        
        return not bracket
            


        