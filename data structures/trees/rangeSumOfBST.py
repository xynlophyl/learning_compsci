from ..implementations.trees import BinaryTreeNode as TreeNode

def rangeSumBST(root, low, high):
  '''
  goal: given a BST, return the sum of all nodes that have values between (inclusive) low and high
  root: TreeNode or None, low: int, high: int
  returns: int
  '''
  s = 0
  if not root:
    return s
  
  def search(curr):
    if not curr:
      return
    
    if curr.val >= low and curr.val <= high:
      s += curr.val
    
    search(curr.left)
    search(curr.right)
    
  search(root)
  return s