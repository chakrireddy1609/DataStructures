class Dup:
    def duplicate(self,nums):
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


d = Dup()
print(d.duplicate([1,2,3,2]))

