from pyraminx import Pyraminx
from pyraminx import pyraminx_state
from randomizer import randomizer
import heapq

# Function to solve the Pyraminx using A*
def a_star_solve(initial_state):
    open_list = []
    closed_list = set()

    heapq.heappush(open_list, initial_state)

    max_iterations = 10000  # Prevent infinite loops or excessive runtime
    iteration = 0

    while open_list and iteration < max_iterations:
        iteration += 1
        current_state = heapq.heappop(open_list)

        if current_state.is_solved():
            print("Solution found.")
            return reconstruct_path(current_state)

        closed_list.add(current_state)

        for child_state in current_state.generate_child_states():
            if child_state in closed_list:
                continue
            if child_state not in open_list:
                heapq.heappush(open_list, child_state)

    print("No solution found after max iterations.")
    return None

# Function to reconstruct the path from the goal to the initial state
def reconstruct_path(state):
    path = []
    while state.parent:
        path.append(state)
        state = state.parent

    return path[::-1]

# Function to run k-randomized puzzles and solve them using A*
def run_k_randomized_puzzles():
    for k in range(3, 4):  # For k from 3 to 20
        print(f"Solving puzzles for k = {k}:")
        for i in range(5):  # Solve 5 puzzles for each k
            # Create and randomize a new Pyraminx
            pyraminx = Pyraminx()
            randomizer(k, pyraminx)  # Randomize Pyraminx with k moves

            # Create the initial state for solving
            initial_state = pyraminx_state(pyraminx, 0)

            # Print the initial heuristic cost
            print(f"Initial h_cost for puzzle {i + 1} (k={k}):", initial_state.h_cost)

            # Solve the puzzle using A*
            solution_path = a_star_solve(initial_state)

            if solution_path:
                print(f"Solution found for puzzle {i + 1} (k={k}) with {len(solution_path)} moves.")
                # Print each step in the solution path
                for step_num, state in enumerate(solution_path):
                    print(f"Step {step_num + 1}:")
                    state.state.print_pyraminx()  # Assuming Pyraminx has a method to print its current state
            else:
                print(f"No solution found for puzzle {i + 1} (k={k}).")

# Run the function to solve puzzles
run_k_randomized_puzzles()
