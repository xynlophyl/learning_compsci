'''
goal: implement a prefix trie to store a dataset of strings that allows for fast prefix and word insert and search
'''

class Trie:
  def __init__(self, val=''):
    self.children = {}

  def insert(self, word: str) -> None:
    curr = self.children
    for c in word:
      if c in curr:
        curr = curr[c].children
      else:
        curr[c] = Trie()
        curr = curr[c].children
    curr['*'] = Trie()

  def search(self, word: str) -> bool:
    curr = self.children
    for c in word:
      if c in curr:
        curr = curr[c].children
      else:
        return False
    return '*' in curr

  def startsWith(self, prefix: str) -> bool:
    curr = self.children
    for c in prefix:
      if c in curr:
        curr = curr[c].children
      else:
        return False
    return True
