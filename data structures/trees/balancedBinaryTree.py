from trees import BinaryTreeNode

def isBalanced(root):
  '''
  goal: check whether tree is balanced (difference in height of left and right subtrees is no greater than 1)
  root: TreeNode or None
  return: bool
  '''
  def getHeight(root):
    if not root:
      return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))
  
  if not root:
    return True
  diff = getHeight(root.right) - getHeight(root.left)
  if diff**2 > 1:
    return False
  
  return isBalanced(root.left) and isBalanced(root.right)
