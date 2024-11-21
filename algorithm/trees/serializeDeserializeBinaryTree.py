from ..implementations.trees import BinaryTreeNode as TreeNode
import collections

class Codec:

  def serialize(self, root):
    '''
    goal: Encodes a tree to a single string.
    root: TreeNode
    return: str
    '''

    # return self.serialize_dfs(root)
    return self.serialize_bfs(root)

  def deserialize(self, data):
    '''
    goal: Decodes your encoded data to tree.
    data: str
    return: TreeNode
    '''
    # return self.serialize_dfs(data)
    return self.serialize_bfs(data)

  # method 1: dfs
  
  def serialize_dfs(self, root):
    if not root:
      return ''
    
    res = []
    def dfs(curr):
      if not curr:
        res.append('*')
      else:
        res.append(str(curr.val))
        dfs(curr.left)
        dfs(curr.right)
      return
    
    dfs(root)
    return ','.join(res)
      

  def deserialize_dfs(self, data):
    if not data:
      return None
    
    vals = data.split(',')
    self.i = 0 
    
    def dfs():
      if vals[self.i] == "*":
        self.i += 1
        return None
      root = TreeNode(int(vals[self.i]))
      self.i += 1
      root.left = dfs()
      root.right = dfs()
      return root
    return dfs()

  # mehtod 2: bfs + iterative rebuild

  def serialize_bfs(self, root):
    if not root:
      return ''
    
    ret = []
    q = collections.deque()
    q.append(root)
    
    while q:
      curr = q.popleft()
      if not curr:
        ret.append('*')
      else:
        ret.append(str(curr.val))
        q.append(curr.left)
        q.append(curr.right)
    return ','.join(ret)
      

  def deserialize_bfs(self, data):
    if not data:
      return None
    
    vals = collections.deque(data.split(','))
    
    q = collections.deque()
    root = TreeNode(int(vals.popleft()))
    q.append(root)
    
    while vals:
      node = q.popleft()
      l = vals.popleft()
      r = vals.popleft()
      if l != "*":
        node.left = TreeNode(int(l))
        q.append(node.left)
      if r != "*":
        node.right = TreeNode(int(r))
        q.append(node.right)
    
    return root