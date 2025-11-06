class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sign_arr = ['+', '-', '*', '/']
        # num_arr = []
        res_stack = []

        for i in range(len(tokens)):
            if tokens[i] not in sign_arr:
                res_stack.append(tokens[i])
            else:
                num_1 = int(res_stack.pop())
                num_2 = int(res_stack.pop())

                res = None
                if tokens[i] == '+':
                    res = num_2 + num_1
                elif tokens[i] == '-':
                    res = num_2 - num_1
                elif tokens[i] == '*':
                    res = num_2 * num_1
                else:
                    res = num_2 / num_1

                res_stack.append(str(int(res)))

        return int(res_stack[0])
