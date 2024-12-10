"""
Santa Claus's elves 🧝🧝‍♂️ have found a bunch of mismatched magic boots in the workshop. Each boot is described by two values:

type indicates if it's a left boot (I) or a right boot (R).
size indicates the size of the boot.
Your task is to help the elves pair all the boots of the same size having a left and a right one. To do this, you should return a list of the available boots after pairing them.

Note: You can have more than one pair of boots of the same size!
"""
from timeit import timeit

# Best performance solution
def organizeShoes(shoes: list[dict]) -> list[int]:
  organized_shoes: dict = {}
  organized_list: list[int] = []
  for elem in shoes:
    foot: str = elem['type']
    size: int = elem['size']
    pair = 'R' if foot == 'I' else 'I'
    if size not in organized_shoes:
      organized_shoes[size] = {foot: 1, pair: 0}
      continue
    if foot not in organized_shoes[size]:
      organized_shoes[size][foot] = 0
    if organized_shoes[size][pair] > 0:
      organized_list.append(size)
      organized_shoes[size][pair] -= 1
    else:
      organized_shoes[size][foot] += 1
  return organized_list

def organizeShoes1(shoes: list[dict]) -> list[int]:
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


# Wrapper to execute the function and capture result
def create_wrapper(name, *args, **kwargs):
  def inner() -> None:
    global result  # global variable to store result
    result = name(*args, **kwargs)
  return inner

result = None
args = ([
  { "type": 'I', "size": 38 },
  { "type": 'I', "size": 38 },
  { "type": 'R', "size": 38 },
  { "type": 'R', "size": 38 },
  { "type": 'I', "size": 38 },
  { "type": 'I', "size": 42 },
  { "type": 'R', "size": 41 },
  { "type": 'R', "size": 42 },
],)

# Warmup
wrapper = create_wrapper(organizeShoes, *args)
execution_time = timeit(wrapper, number=100000)

# Performance test
for function_name in (organizeShoes, organizeShoes1):
  wrapper = create_wrapper(function_name, *args)
  times = 100_000
  print(f"{function_name.__name__:} took average {timeit(wrapper, number=times) / times*1000:.8f} microsec. Result:\n{result}")

# Example
# print(organizeShoes(args))