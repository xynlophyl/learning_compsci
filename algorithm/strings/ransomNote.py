def canConstruct(ransomNote, magazine):
  '''
  goal: check if ransom note can be formed using characters from magazine (each character can only be used once)
  ransomNote: str, magazine: str
  return: bool 
  '''
  if len(ransomNote) > len(magazine):
    return False

  # solution 2
  d = {}
  for c in magazine:
    d[c] = d.get(c,0) + 1

  for c in ransomNote:
    if c in d:
      if d[c] < 1:
        return False
      d[c] -= 1
    else:
      return False
  return True      

  # solution 1
  note_d, mag_d = {}, {}
  for c in ransomNote:
    note_d[c] = note_d.get(c,0) + 1
  for c in magazine:
    mag_d[c] = mag_d.get(c,0) + 1
    
  for c in note_d:
    if mag_d.get(c,0) < note_d[c]:
      return False
  return True
