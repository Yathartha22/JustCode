# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traverse(root, k):
    global index, res 
    if not root:
        # index += 1
        return None
    
    traverse(root.left, k)
    
    index += 1
    if index == k:
        res = root.val
    # print(index, root.val)
    
    traverse(root.right, k)
    
index = 0
res = None
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global index, res
        index= 0
        traverse(root, k)
        return res
