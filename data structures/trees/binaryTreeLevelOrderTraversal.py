from trees import BinaryTreeNode as TreeNode
def levelOrder(root):
  '''
  goal: return a list of values in the given tree, root, where each level is separated into it's own list
  root: TreeNode or None
  return: list[list[int]]
  '''
  if not root:
    return []
  
  queue = [root]
  res = []
  while queue:
    queue_count = len(queue)
    level = []
    for i in range(queue_count):
      curr = queue.pop(0)
      if curr:
        level.append(curr.val)
        queue.append(curr.left)
        queue.append(curr.right)
    if level:
      res.append(level)
  return res
  