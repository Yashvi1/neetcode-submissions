class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        res = False
        open_bracket = "({["
        close_brackets = ")}]"
        order = []
        count = 0
        for ch in s:
            if ch in open_bracket:
                print("in open brackt")
                order.append(ch)
                count += 1
            elif len(order) > 0 and (brackets[order.pop()] == ch):
                print("popping")
                count -= 1
            else:
                return False
        return count == 0 