class Solution(object):
    def isValid(self, s):
        stack=[]
        open="[{("
        for c in s:
            if c in open:
                stack.append(c)
            else:
                if not stack or (c==')' and stack[-1]!= '(')or (c == '}' and stack[-1] != '{') or (c == ']' and stack[-1] != '['):
                    return False
                stack.pop()
        return not stack

        """
        :type s: str
        :rtype: bool
        """
        