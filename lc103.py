# 103. Binary Tree Zigzag Level Order Traversal
# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).

# The idea to solve to question is, we treat ziazaglevel order as level order first.
# return a list for level order traversal, then using a loop to reverse odd depth in the list of list.
# TimeComplexity is O(N), Space is O(N)
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        self.helper(root, 0, result)
        for i in range(len(result)):
            if i % 2 != 0:
                result[i] = result[i][::-1]
        return result

    def helper(self, node, level, result):
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        if node.left:
            self.helper(node.left, level + 1, result)
        if node.right:
            self.helper(node.right, level + 1, result)

