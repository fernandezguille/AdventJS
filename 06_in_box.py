"""
We have already wrapped hundreds of presents 🎁… but an elf forgot to check if the present, represented by an asterisk *, is inside the box.

The box has a present (*) and counts as "inside the box" if:

It is completely surrounded by # on the box's edges.
The * is not on the box's edges.
Keep in mind that the * can be inside, outside, or may not even be there. We must return true if the * is inside the box and false otherwise.
"""
def in_box(box: list[str]) -> bool:
  found = False
  for char in box[0] + box[-1]:
    if char != "\u0023":
      return False
  for line in box[1:-1]:
    if not line.startswith("\u0023") or not line.endswith("\u0023"):
      return False
    if "*" in line:
      found = True
  return found

# Example
print(in_box([
  "#####",
  "#   #",
  "#  *#",
  "#####"
]))