"""
Santa Claus's elves 🧝🧝‍♂️ have found a bunch of mismatched magic boots in the workshop. Each boot is described by two values:

type indicates if it's a left boot (I) or a right boot (R).
size indicates the size of the boot.
Your task is to help the elves pair all the boots of the same size having a left and a right one. To do this, you should return a list of the available boots after pairing them.

Note: You can have more than one pair of boots of the same size!
"""
def organizeShoes(shoes: list[dict]) -> list[int]:
  organized_shoes: dict = {}
  organized_list: list[int] = []
  for elem in shoes:
    foot: str = elem['type']
    size: int = elem['size']
    if size not in organized_shoes:
      organized_shoes[size] = {}
    if foot not in organized_shoes[size]:
      organized_shoes[size][foot] = 0
    organized_shoes[size][foot] += 1
  for sizes, feet in organized_shoes.items():
    if len(feet) == 2:
      organized_list.extend([sizes] * min(feet.values()))
  return organized_list

# Example
print(organizeShoes([
  { "type": 'I', "size": 38 },
  { "type": 'I', "size": 38 },
  { "type": 'R', "size": 38 },
  { "type": 'R', "size": 38 },
  { "type": 'I', "size": 42 },
  { "type": 'R', "size": 41 },
  { "type": 'R', "size": 42 },
]))