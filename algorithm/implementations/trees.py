'''
Class Implementation
'''
class BinaryTreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
search algorithms
'''
def breadthFirstSearch(root, val):
    queue = [root]
    while queue:
        curr = queue.pop()
        if curr:
            if curr.val == val:
                return curr
            queue.append(curr.left)
            queue.append(curr.right)
    return -1

def depthFirstSearch(root,val):
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr:
            if curr.val == val:
                return curr
            stack.append(curr.left)
            stack.append(curr.right)
    return -1

def bfs_recur(root,val):
    if not root:
        return -1
    if root.val == val:
        return root
    l = bfs_recur(root.left, val)
    if l != -1:
        return l
    return bfs_recur(root.right, val)


    
'''
example questions
'''
def getHeight(root):
    if not root:
        return 0
    return max(getHeight(root.left), getHeight(root)) + 1

def invertTree(root):
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
