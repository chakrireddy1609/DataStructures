class Solution:

    def calculator(self):
        operator = input("Enter an operator : ")
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))

        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "%":
            return num1 % num2
        elif operator == "/":
            return num1/num2
        else:
            return "invalid operator"


s = Solution()
print(s.calculator())

