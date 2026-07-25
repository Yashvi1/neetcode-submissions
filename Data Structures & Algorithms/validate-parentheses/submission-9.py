class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        res = False
        open_bracket = "({["
        order = []
        for ch in s:
            if ch in open_bracket:
                print("in open brackt")
                order.append(ch)
            elif len(order) > 0 and (brackets[order.pop()] == ch):
                print("popping")
            else:
                return False
        return len(order) == 0 