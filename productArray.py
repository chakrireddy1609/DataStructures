class Product_Array:
    def prod(self,nums):
        prod_new = []
        product = 1
        for i in nums:
            product *= i
        for j in nums:
            prod_new.append(product//j)
        print(prod_new)




pa = Product_Array()
pa.prod([1,2,3,4,5])
