from ..implementations.trees import BinaryTreeNode as TreeNode

def kthSmallest(root, k):
  '''
  goal: find the k-th smallest element of the given BST
  root: TreeNode or None, k: int
  return: int
  '''

  n = 0
  stack = []
  curr = root
  
  while curr or stack:
    while curr:
      stack.append(curr)
      curr = curr.left
      
    curr = stack.pop()
    n += 1
    if n == k:
      return curr.val
    curr = curr.right
    