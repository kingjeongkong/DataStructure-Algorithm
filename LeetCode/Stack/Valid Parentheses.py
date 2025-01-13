class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        balance = True

        for s in s:
            if s == '(' or s == '{' or s == '[':
                stack.append(s)
            elif s == ')':
                if not stack or stack[-1] != '(':
                    balance = False
                    break
                stack.pop()
            elif s == '}':
                if not stack or stack[-1] != '{':
                    balance = False
                    break
                stack.pop()
            elif s == ']':
                if not stack or stack[-1] != '[':
                    balance = False
                    break
                stack.pop()

        if stack:
            balance = False

        return balance

# Same as the 균형잡힌 세상(백준)

# Main point is declaring balance(boolean) and while validating the logic, if the input isn' valid and balance is false even once, break that loop and return the balance