class BalancedParen:

    def is_Valid(self,s):
        stack = []
        hashm = {")":"(","{":"}","]":"["}
        for c in s:
            if c in hashm:
                if stack and stack[-1] == hashm[c]:
                    return True
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

b = BalancedParen()
print(b.is_Valid("[]"))