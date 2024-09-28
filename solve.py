from pyraminx import Pyraminx
from pyraminx import pyraminx_state
from randomizer import randomizer
from pyraminx import tile
import heapq

pyraminx = Pyraminx()
randomizer(1, pyraminx)
state = pyraminx_state(pyraminx, 0)
print(state.h_cost)

def a_star_solve(initial_state: pyraminx_state):
    open_list = []
    closed_list = set()

    heapq.heappush(open_list, initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_solved():
            print("Current state is goal")
            return reconstruct_path(current_state)
        
        closed_list.add(current_state.state)

        for child_state in current_state.generate_child_states():
            if child_state.state in closed_list:
                continue
            if child_state not in open_list:
                heapq.heappush(open_list, child_state)

def reconstruct_path(state):
    path = []
    while state.parent:
        path.append(state)
        state = state.parent
    
    return path[::-1]

a_star_solve(state)