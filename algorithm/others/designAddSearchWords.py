'''
goal: implement a structure to add words and search if a word has already been added
'''

class WordDictionary:
  def __init__(self):
    self.children = {}

  def addWord(self, word: str) -> None:
    if not word:
      self.children['*'] = WordDictionary()
      return
    
    if word[0] not in self.children:
      self.children[word[0]] = WordDictionary()
    self.children[word[0]].addWord(word[1:])
    return

  def search(self, word: str) -> bool:
    if not word:
      return '*' in self.children
    
    if word[0] == '.':
      for child in self.children:
        if self.children[child].search(word[1:]):
          return True
    else:
      if word[0] in self.children:
        return self.children[word[0]].search(word[1:])
    return False
