from ..implementations.trees import BinaryTreeNode as TreeNode

def inorderTraversal(root):
  '''
  goal: return the in-order traversal of the binary tree
  root: TreeNode or None
  returns: list[int]
  '''

  if not root:
    return []
  
  # iterative
  ret = []
  stack = []
  curr = root
  
  while stack or curr:
    while curr:
      stack.append(curr)
      curr = curr.left
    
    curr = stack.pop()
    ret.append(curr.val)
    curr = curr.right
  
  return ret
  
  # recursive
  self.ret = []
  def search(root):
    if not root:
      return
    
    search(root.left)
    self.ret.append(root.val)
    search(root.right)
  
  search(root)
  return self.ret
    