from ..implementations.trees import BinaryTreeNode as TreeNode
    
def postorderTraversal(root):
  '''
  goal: return the in-order traversal of the binary tree
  root: TreeNode or None
  returns: list[int]
  '''
  if not root:
    return []
  
  # iterative
  
  # recursive
  ret = []

  def search(root):
    if not root:
      return
    
    search(root.left)
    search(root.right)
    ret.append(root.val)
  
  search(root)
  return ret