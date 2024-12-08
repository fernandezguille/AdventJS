"""
It's time to select the fastest reindeer for Santa's journeys! 🦌🎄
Santa Claus has organized exciting reindeer races to determine which ones are in the best shape.

Your task is to display each reindeer's progress on a snow track in isometric format.

The information you receive:

indices: An array of integers representing each reindeer's progress on the track:
0: The lane is empty.
Positive number: The reindeer's current position from the beginning of the track.
Negative number: The reindeer's current position from the end of the track.
length: The length of each lane.
Return a string representing the race track:

Each lane has exactly length positions filled with snow (~).
Each reindeer is represented with the letter r.
Lanes are numbered at the end with /1, /2, etc.
The view is isometric, so the lower lanes are shifted to the right.
"""
# def draw_race(indices: list[int], length: int) -> str:
#   fixed_indices: list[int] = [index if index >= 0 else length+index for index in indices]
#   lanes: list[str] = []
#   total_lanes: int = len(fixed_indices)
#   for number, reindeer_position in enumerate(fixed_indices, 1):
#     lane: str = " "*(total_lanes-number) + "".join("~" if i != reindeer_position or i == 0 else 'r' for i in range(length)) + f" /{number}"
#     lanes.append(lane)
#   return "\n".join(lanes)

def draw_race(indices: list[int], length: int) -> str:
  total_lanes: int = len(indices)
  lanes: list[str] = []
  for number, reindeer_position in enumerate(indices, 1):
    lane: list[str] = ["~"] * length
    if reindeer_position != 0:
      lane[reindeer_position] = "r"
    str_lane: str = " "*(total_lanes-number) + ''.join(lane) + f" /{number}"
    lanes.append(str_lane)
  return '\n'.join(lanes)

# Example
print(draw_race([2, -1, 0, 5, -3], 10))