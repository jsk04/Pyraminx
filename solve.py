from pyraminx import Pyraminx
from pyraminx import pyraminx_state
from randomizer import randomizer
import heapq
import matplotlib.pyplot as plt

# Function to solve the Pyraminx using A*
def a_star_solve(initial_state):
    open_list = []
    closed_list = set()

    heapq.heappush(open_list, initial_state)

    max_iterations = 1000  # Prevent infinite loops or excessive runtime
    iteration = 0
    nodes_expanded = 0  # Counter for the number of nodes expanded

    while open_list and iteration < max_iterations:
        iteration += 1
        current_state = heapq.heappop(open_list)
        nodes_expanded += 1

        if current_state.is_solved():
            print("Solution found.")
            return reconstruct_path(current_state), nodes_expanded

        closed_list.add(current_state)

        for child_state in current_state.generate_child_states():
            if child_state in closed_list:
                continue
            if child_state not in open_list:
                heapq.heappush(open_list, child_state)

    print("No solution found after max iterations.")
    return None, nodes_expanded

# Function to reconstruct the path from the goal to the initial state
def reconstruct_path(state):
    path = []
    while state.parent:
        path.append(state)
        state = state.parent

    return path[::-1]

# Function to run k-randomized puzzles and solve them using A*
def run_k_randomized_puzzles():
    k_values = list(range(3, 10))  # For k from 3 to 8
    average_nodes_expanded_per_k = []

    for k in k_values:
        print(f"Solving puzzles for k = {k}:")
        nodes_expanded_list = []

        for i in range(5):  # Solve 5 puzzles for each k
            # Create and randomize a new Pyraminx
            pyraminx = Pyraminx()
            randomizer(k, pyraminx)  # Randomize Pyraminx with k moves

            # Create the initial state for solving
            initial_state = pyraminx_state(pyraminx, 0)

            # Print the initial heuristic cost
            print(f"Initial h_cost for puzzle {i + 1} (k={k}):", initial_state.h_cost)

            # Solve the puzzle using A*
            solution_path, nodes_expanded = a_star_solve(initial_state)
            nodes_expanded_list.append(nodes_expanded)

            if solution_path:
                print(f"Solution found for puzzle {i + 1} (k={k}) with {len(solution_path)} moves.")
                # Print each step in the solution path
                for step_num, state in enumerate(solution_path):
                    print(f"Step {step_num + 1}:")
                    state.state.print_pyraminx()  # Assuming Pyraminx has a method to print its current state
            else:
                print(f"No solution found for puzzle {i + 1} (k={k}).")
                print("Puzzle configuration that failed to solve:")
                pyraminx.print_pyraminx()  # Print the scrambled Pyraminx configuration

        # Calculate average nodes expanded for current k
        average_nodes_expanded = sum(nodes_expanded_list) / len(nodes_expanded_list)
        average_nodes_expanded_per_k.append(average_nodes_expanded)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, average_nodes_expanded_per_k, marker='o', linestyle='-', color='b')
    plt.xlabel('Number of Random Moves (k)')
    plt.ylabel('Average Number of Nodes Expanded')
    plt.title('Average Number of Nodes Expanded vs. Number of Random Moves (k)')
    plt.grid(True)
    plt.show()

# Run the function to solve puzzles and generate the plot
run_k_randomized_puzzles()

