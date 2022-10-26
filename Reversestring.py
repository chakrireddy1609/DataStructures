def revstr(lst):

# Use two pointer method
    l = 0
    r = len(lst)-1

    while l < r:
        lst[l],lst[r] = lst[r],lst[l]
        l,r = l+1, r-1
    return lst


# Use stack
def revstrstack(lst1):
    stack = []
    for i in lst1:
        stack.append(i)
    j = 0
    while stack:
        lst1[j] = stack.pop()
        j += 1
    return lst1

#use recursion
def revstr_recursion(l,r,lst2):
    if l<r:
        lst2[l],lst2[r] = lst2[r],lst2[l]
        revstr_recursion(l+1,r-1)
    return lst2


print(revstr(["h","e","l","l","o"]))
print(revstrstack(["h","e","l","l","o"]))
print(revstr_recursion(["h","e","l","l","o"]))