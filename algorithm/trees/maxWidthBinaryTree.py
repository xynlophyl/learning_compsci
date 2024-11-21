from ..implementations.trees import BinaryTreeNode as TreeNode

def widthOfBinaryTree(root):
  '''
  goal: find the binary tree's maximum width (distance between left and right most nodes on the same level)
  root: TreeNode or None
  return: int
  '''
  if not root:
    return 0
  
  queue = [(root, 1)]
  max_width = -float('inf')
  while queue:
    n = len(queue)
    l = float('inf')
    h = -float('inf')
    for i in range(n):
      curr, idx = queue.pop(0)
      if curr:
        l = min(l, idx)
        h = max(l,idx)
        queue.append((curr.left, idx*2-1))
        queue.append((curr.right, idx*2))
    max_width = max(max_width, h-l+1)
  
  return max_width if max_width != -float('inf') else 0
  