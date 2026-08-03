class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evaluate = []
        op = "+-*/"

        for t in tokens:
            if t in op:
                first = int(evaluate.pop())
                second = int(evaluate.pop())
                match t:
                    case "+":
                        evaluate.append(first+second) 
                    case "-":
                        evaluate.append(second-first)
                    case "*":
                        evaluate.append(first*second)
                    case "/":
                        if first == 0:
                            evaluate.append(second)
                        elif second == 0:
                            evaluate.append(0)

                        else:
                            evaluate.append(second/first)
                    case _:
                        return
                print(evaluate)
            else:
                evaluate.append(t)
               
        
        return int(evaluate.pop())

        