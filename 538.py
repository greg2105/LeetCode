# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # want to do a DFS, finding the right most node first. Add to sum, and traverse the tree adding the sum
        # to each 'visited' node

        # use this to keep track of how we should add to each node
        self.sum = 0

        def reverse_in_order(node):
            if not node:
                return
            
            # prioritize right nodes, because we want to explore in descending order
            reverse_in_order(node.right)

            # first add the sum to the node, then set the sum to the new node value
            node.val += self.sum
            self.sum = node.val

            # go left if there are no right nodes to explore
            reverse_in_order(node.left)

        reverse_in_order(root)

        # return the updated tree
        return root
