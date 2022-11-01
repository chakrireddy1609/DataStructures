class Solution:

    def heightBT(self,node):
        if node is None:
            return -1

        left_height = self.heightBT(node.left)
        right_height = self.heightBT(node.right)

        return 1 + max(left_height,right_height)


