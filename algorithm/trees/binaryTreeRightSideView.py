from ..implementations.trees import BinaryTreeNode as TreeNode

def rightSideView(root):
  '''
  goal: return a list of the values of the right most node at each level
  root: TreeNode or None
  return: list[int]
  '''
  if not root:
    return []
  
  queue = [root]
  ret = []
  while queue:
    n = len(queue)
    most_right = None
    for i in range(n):
      curr = queue.pop(0)
      if curr:
        queue.append(curr.right)
        queue.append(curr.left)
        if most_right == None:
          most_right = curr.val
    if most_right != None:
      ret.append(most_right)
  return ret
