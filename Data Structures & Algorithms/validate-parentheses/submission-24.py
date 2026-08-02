class Solution:
    
    def isValid(self, s: str) -> bool:
        pair = {
        "{":"}",
        "(":")",
        "[":"]"
        }

        bracket = []
        for b in s:
            if b in pair:
                bracket.append(b)
            elif b not in pair:
                if not bracket:
                    return False
                if pair[bracket[-1]] != b:
                    return False
                else:
                    bracket.pop()
        
        return not bracket
            


        