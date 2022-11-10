from ..implementations.trees import BinaryTreeNode as TreeNode

def preorderTraversal(root):
  '''
  goal: return the pre-order traversal of the binary tree
  root: TreeNode or None
  returns: list[int]
  '''

  if not root:
    return []
  
  # iterative solution: O(n)

  ret = []
  stack = [root]
  
  while stack:
    curr = stack.pop()
    if not curr:
      continue
    ret.append(curr.val)
    stack.append(curr.right)
    stack.append(curr.left)
  return ret
  

  # recursive solution: O(n)
  if not root:
    return []

  self.ret = []

  def search(root):
    if not root:
      return

    self.ret.append(root.val)
    search(root.left)
    search(root.right)

  search(root)
  return self.ret