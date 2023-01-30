class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = "([{"
        close = ")]}"

        for sym in s:
            if sym in open:
                # print("open paren appending", sym)
                stack.append(sym)
            else:
                # print("close paren", sym)
                if len(stack) == 0: return False

                last = stack.pop()
                if ((sym == ")" and last == "(") or (sym == "}" and last == "{") or (sym == "]" and last == "[")):
                    # print('matching - closing')
                    pass
                else:
                    # print('invalid')
                    return False

        return True if len(stack) == 0 else False