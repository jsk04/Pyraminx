from pyraminx import Pyraminx
from pyraminx import pyraminx_state
from randomizer import randomizer
from pyraminx import tile

pyraminx = Pyraminx()

pyraminx.rotate_front_rows(True, 1)
pyraminx.rotate_front_rows(False, 2)
pyraminx.rotate_diagonal_layer(1, True, 1)
pyraminx.rotate_diagonal_layer(1, False, 1)
pyraminx.rotate_front_rows(True, 2)
pyraminx.rotate_front_rows(False, 1)
current_state = pyraminx_state(pyraminx, 0)
print(current_state.h_cost)
# current_state.state.rotate_diagonal_layer(1, False, 1)
# print(current_state.h_cost)
# child_states = state.generate_child_states()
# for tile in pyraminx.blue_tiles[1]:
#     print(tile.fixed_place)

# pyraminx.print_pyraminx()
# for face in pyraminx.faces:
#     print(face[0][0].move_stack)
#     print("\n")

# pyraminx.rotate_front_rows(True, 1)
# print(pyraminx.red_tiles[0][0].move_stack)
# print(pyraminx.blue_tiles[0][0].move_stack)
# print(pyraminx.yellow_tiles[0][0].move_stack)
# print(pyraminx.green_tiles[0][0].move_stack)

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
# print(f"This is what's in green tip: ", pyraminx.green_face[0][0].position)

# pyraminx.rotate_front_rows(True, 1)
# print(pyraminx.red_tiles[0][0].move_stack)
# print(pyraminx.blue_tiles[0][0].move_stack)
# print(pyraminx.yellow_tiles[0][0].move_stack)
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
