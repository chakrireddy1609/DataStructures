class BalancedParen:

    def __init__(self):
        self.bracketarr = []

    def checkBalance(self, paren_string):
        is_balanced = True

        for i in range(len(paren_string)):
            if is_balanced:
                if paren_string[i] in "([{":
                    self.bracketarr.append(paren_string[i])
                else:
                    if len(self.bracketarr) == 0:
                        is_balanced = False
                    else:
                        top = list(paren_string).pop()
                        if top == ")" and self.bracketarr[i] == "(":
                            is_balanced = True
                        elif top == "]" and self.bracketarr[i] == "[":
                            is_balanced = True
                        elif top == "}" and self.bracketarr[i] == "{":
                            is_balanced = True
                        else:
                            is_balanced = False
                    return is_balanced
            else:
                return False

        if len(self.bracketarr) == 0 and is_balanced:
            return True
        else:
            return False


b1 = BalancedParen()
print(b1.checkBalance("[[{(]]"))

