class Solution(object):
    def isValid(self, s):

        stack = []

        for current in s:

            if current in "({[":
                stack.append(current)

            else:

                if len(stack) == 0:
                    return False

                if current == ")" and stack[-1] == "(":
                    stack.pop()

                elif current == "}" and stack[-1] == "{":
                    stack.pop()

                elif current == "]" and stack[-1] == "[":
                    stack.pop()

                else:
                    return False

        return len(stack) == 0