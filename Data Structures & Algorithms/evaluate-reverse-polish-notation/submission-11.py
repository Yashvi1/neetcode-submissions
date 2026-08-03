class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evaluate = []
        op = "+-*/"

        for t in tokens:
            print('inside for')
            if t in op:
                print('inside if')
                first = int(evaluate.pop())
                second = int(evaluate.pop())
                print(f"first={first} second={second}")
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
                print('inside else')
                evaluate.append(t)
                print(evaluate)
        print(evaluate)
        return int(evaluate.pop())

        