class DecToBinary():
    def __init__(self):
        self.rem = []

    def decbin(self,dec_num):
        while dec_num > 0:
            remainder = dec_num%2
            self.rem.append(remainder)
            dec_num = dec_num//2

        bin_num = ""
        while len(self.rem) != 0:
            bin_num += str(self.rem.pop())
        return bin_num


s1 = DecToBinary()
print(s1.decbin(242))

