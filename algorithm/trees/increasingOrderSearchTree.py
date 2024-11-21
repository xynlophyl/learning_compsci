from ..implementations.trees import BinaryTreeNode as TreeNode

def increasingBST(root):
  '''
  goal: given a BST, rearrange the tree in-order such that the left-most node is the new root, and every node only has a right child
  root: TreeNode
  return: TreeNode 
  '''
  queue = []

  def inorder(root):
    if not root:
      return

    inorder(root.left)
    queue.append(root)
    inorder(root.right)
  
  inorder(root)
  
  dummy = TreeNode()
  curr = dummy
  for node in queue:
    curr.right = node
    curr = curr.right
    curr.left = None


  return dummy.right
      