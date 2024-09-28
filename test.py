from pyraminx import Pyraminx
from randomizer import randomizer
from pyraminx import tile

pyraminx = Pyraminx()

# for tile in pyraminx.blue_tiles[1]:
#     print(tile.fixed_place)

# pyraminx.print_pyraminx()
# for face in pyraminx.faces:
#     print(face[0][0].move_stack)
#     print("\n")

pyraminx.rotate_front_rows(True, 1)
print(pyraminx.red_tiles[0][0].move_stack)
print(pyraminx.blue_tiles[0][0].move_stack)
print(pyraminx.yellow_tiles[0][0].move_stack)
# print(pyraminx.green_tiles[0][0].move_stack)

pyraminx.rotate_front_rows(True, 1)
print(pyraminx.red_tiles[0][0].move_stack)
print(pyraminx.blue_tiles[0][0].move_stack)
print(pyraminx.yellow_tiles[0][0].move_stack)
# print(f"This is what's in red tip: ", pyraminx.red_face[0][0].position)
# print(f"This is what's in red tip's stack: ", pyraminx.red_face[0][0].move_stack)
# print(f"This is what's in blue tip: ", pyraminx.blue_face[0][0].position)
# print(f"This is what's in blue tip's stack: ", pyraminx.blue_face[0][0].move_stack)
# print(f"This is what's in yellow tip: ", pyraminx.yellow_face[0][0].position)
# print(f"This is what's in yellow tip's stack: ", pyraminx.yellow_face[0][0].move_stack)
# print(f"This is what's in green tip: ", pyraminx.green_face[0][0].position)

pyraminx.rotate_front_rows(True, 1)
print(pyraminx.red_tiles[0][0].move_stack)
print(pyraminx.blue_tiles[0][0].move_stack)
print(pyraminx.yellow_tiles[0][0].move_stack)
# pyraminx.rotate_front_rows(True, 1)
# print(pyraminx.red_tiles[0][0].move_stack)
# print(pyraminx.blue_tiles[0][0].move_stack)
# print(pyraminx.yellow_tiles[0][0].move_stack)
# print(f"This is what's in red tip: ", pyraminx.red_face[0][0].position)
# print(f"This is what's in red tip's stack: ", pyraminx.red_face[0][0].move_stack)
# print(f"This is what's in blue tip: ", pyraminx.blue_face[0][0].position)
# print(f"This is what's in blue tip's stack: ", pyraminx.blue_face[0][0].move_stack)
# print(f"This is what's in yellow tip: ", pyraminx.yellow_face[0][0].position)
# print(f"This is what's in yellow tip's stack: ", pyraminx.yellow_face[0][0].move_stack)

# pyraminx.print_pyraminx()
