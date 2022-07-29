from trees import BinaryTreeNode as TreeNode

def isValidBST(root):
  '''
  goal: returns whether given tree is a binary search tree (left descendants < curr node < right descendants)
  root: TreeNode
  return: bool
  '''
  def helper(low, root, high):
    if not root:
      return True
    if root.val > low and root.val < high: # making sure node val is within bounds of parents/ ancestors
      return helper(low, root.left, root.val) and helper(root.val, root.right, high)
  if not root:
    return True
  return helper(float('-inf'), root, float('inf'))