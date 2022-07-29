from trees import BinaryTreeNode

memo = {}
def diameterOfBinaryTree(root):
  '''
  goal: find the length of the longest path between two connected nodes in the given binary tree
  root: TreeNode or None
  return: int
  '''
  def getHeight(root):
    if not root:
      return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))
  
  if not root:
    return 0
  if root.val not in memo:
    d = getHeight(root.left) + getHeight(root.right)
    max_d = max(d, diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right))
    memo[root.val] = max_d
  return memo[root.val]
  