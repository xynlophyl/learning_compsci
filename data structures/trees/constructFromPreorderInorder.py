from trees import BinaryTreeNode as TreeNode
def buildTree(preorder, inorder):
  '''
  goal: given list of preorder and inorder traversals of a tree, build the tree out and return its root
  preorder: list[int], inorder: list[int]
  return: TreeNode or None
  '''
  if not preorder or not inorder:
    return None
  
  curr = preorder[0]
  i = inorder.index(curr)
  
  root = TreeNode(curr)
  root.left = buildTree(preorder[1:i+1], inorder[:i])
  root.right = buildTree(preorder[i+1:], inorder[i+1:])
  
  return root
