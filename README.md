***Pyraminx Solver Project***

**Overview**
This project is a Python-based solution to solve the Pyraminx puzzle using the A* search algorithm. It involves various components, including data representation of the Pyraminx, a randomizer for scrambling the puzzle, and an A* solver that utilizes a heuristic function to find the solution. The code also generates metrics such as the average number of nodes expanded during the solution process.

**The project is divided into the following main scripts:**

**main.py**: Used to interactively manipulate the Pyraminx puzzle, including scrambling and rotating the pieces manually.
**solve.py**: Uses the A* algorithm to solve the Pyraminx for a randomized number of moves.
**pyraminx.py**: Contains the data structures and methods representing the Pyraminx puzzle.
**randomizer.py**: Provides functions to randomize the Pyraminx with a user-specified number of moves.

***Project Structure***
**pyraminx.py**: Defines the classes for representing the Pyraminx structure.
        Sticker class to represent each sticker on the Pyraminx.
        Pyraminx class to create the Pyraminx object with four different colored faces.
**randomizer.py**: Provides the randomizer() function to scramble the Pyraminx using both horizontal and diagonal moves.
**main.py**: Allows interactive rotation of the Pyraminx and provides a GUI to make moves and visualize changes.
**solve.py**: Implements the A* algorithm to solve a scrambled Pyraminx and plots the average number of nodes expanded for different scrambles.

***Prerequisites***
    Python 3.6 or later
    Matplotlib (for plotting results)

Ensure the following Python files are present in the same directory:
    pyraminx.py
    randomizer.py
    solve.py
    main.py

Install the necessary dependencies using:

    bash
    Copy code
    pip install matplotlib

***Instructions***
**Running main.py**
main.py is used to interactively rotate the Pyraminx puzzle.

To run main.py:

1. Navigate to the project directory.

Run the following command in terminal:

    python main.py

2. The script will activate a GUI that provides the following options:

- Choose to start with the Pyraminx in the solved state or scramble it by a specified number of moves.
- Visualize the Pyraminx in its current state.
- Make rotations, including horizontal and diagonal rotations of various layers.

3. Follow the on-screen prompts to rotate or quit the program:

- Choose a rotation type (horizontal or diagonal).
- Specify the layer and direction (clockwise or counterclockwise).
- Visualize the new Pyraminx state.

**Running solve.py**
solve.py runs the A* algorithm to solve the Pyraminx.

To run solve.py:

1. Modify parameters as needed in the script:
        max_iterations: This controls how many iterations (nodes expanded) the A* algorithm will allow before terminating.
        k_values: Controls the scramble depth range (k) for the number of random moves used to scramble the Pyraminx.
2. Save the changes to the script.

Run the script using the following command:

    python solve.py

3. The script will:
- Randomly scramble the Pyraminx using the specified k value.
- Use the A* algorithm to find a solution.
- Plot the average number of nodes expanded against the number of random moves (k).

**Summary of Files**
    main.py: Provides an interactive interface to manipulate and visualize the Pyraminx puzzle.
    solve.py: Solves the Pyraminx using A* and plots the average number of nodes expanded, allowing users to see the computational requirements as the scramble complexity (k) increases.
    pyraminx.py: Defines the structure and representation of the Pyraminx. Contains methods for initializing the Pyraminx and representing its state.
    randomizer.py: Contains methods for randomizing the Pyraminx, allowing for controlled scrambles.

***Heuristic***
The heuristic function used in the A* algorithm tracks the highest number of necessary moves required for any given sticker to return to its initial position. It ensures that the estimated cost is always admissible, meaning it will never underestimate the cost to reach the solution.

For more details, refer to the documentation in the PDFs provided.

***Learning Outcomes***
The project highlights:

- The importance of choosing the appropriate data structures for efficient representation.
- Implementation of admissible heuristics for guiding A* effectively.
- Challenges in designing and optimizing heuristics to minimize computational overhead.

**Notes**
Ensure all Python files are in the same directory for imports to work properly.
The complexity of the Pyraminx increases with more random moves, impacting the time and memory requirements of the A* algorithm.
The provided heuristic was chosen for its balance between computational efficiency and accuracy.