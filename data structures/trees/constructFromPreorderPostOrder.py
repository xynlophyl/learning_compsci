from trees import BinaryTreeNode as TreeNode
def buildTree(inorder, postorder):
  '''
  goal: given list of inorder and postorder traversals of a tree, build the tree out and return its root
  inorder: list[int], postorder: list[int]
  return: TreeNode or None
  '''

  if not inorder or not postorder:
    return None
  
  curr = postorder.pop()
  mid = inorder.index(curr)
  
  root = TreeNode(curr)
  root.left = buildTree(inorder[:mid], postorder[:mid])
  root.right = buildTree(inorder[mid+1:], postorder[mid:])
  
  return root