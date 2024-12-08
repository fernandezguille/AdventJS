"""
It's time to put up the Christmas tree at home! 🎄 But this year we want it to be special. We're going to create a function that receives the height of the tree (a positive integer between 1 and 100) and a special character to decorate it.

The function should return a string that represents the Christmas tree, constructed as follows:

The tree is made up of triangles of special characters.
The spaces on the sides of the tree are represented with underscores _.
All trees have a trunk of two lines, represented by the # character.
The tree should always have the same length on each side.
You must ensure the tree has the correct shape using line breaks \n for each line.
"""
def createXmasTree(height: int, ornament: str) -> str:
  max_len = height-1
  tree = "\n".join(("_"*(max_len-i)+ornament*(1+(i*2))+"_"*(max_len-i)) for i in range(height))
  trunk = ("\n"+"_"*max_len+"#"+"_"*max_len)
  return tree + trunk * 2

def createXmasTree2(height: int, ornament: str) -> str:
  tree: str = "\n".join((f'{ornament*(1+(i*2)):_^{height*2-1}}' for i in range(height)))
  trunk: str = f'\n{"#":_^{height*2-1}}'
  return tree + trunk * 2

# Example
print(createXmasTree(5, '*'))
print(createXmasTree2(5, '+'))