# Maze-solver
This project is a Python-based maze solver that utilizes the Breadth-First Search (BFS) algorithm. Unlike Depth-First Search, this solver is guaranteed to find the shortest possible path from the start to the goal in any given maze.   

**Breadth First Search:**
  Breadth-First Search is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or the start point 'A' in our maze) and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

    Optimal: It always finds the shortest path.

    Complete: If a solution exists, BFS will find it.

    Memory: It uses a Queue (FIFO) to manage the frontier, ensuring that the closest nodes are processed first.

**Installation & Setup:**

    Clone the repository:
    git clone https://github.com/livi-git/Maze-solver.git
    cd Maze-solver

    Ensure Python is installed:
    This script requires Python 3.x.

**Usage:**

To solve a maze, paste the maze in maze_text.txt file:
Bash

python main.py

Input Format

The solver reads .txt files where:

    # = Wall

    A = Starting Point

    B = Goal

      = Open Space

**How the Algorithm Works** 

1. Initialization: Place the starting node A into a Queue.
2. Exploration: * Pop the first node from the queue.If it is the goal B, we are done!
   Otherwise, add all adjacent, unvisited     nodes (Up, Down, Left, Right) to the back of the queue and mark them as           explored.
3. Shortest Path: Because we explore all nodes at distance $d$ before moving to $d+1$, the first time we hit the goal, we       have found the most efficient route.

**Console Output:**
```------------------------------------
#  #  #  #  #  #  #  #  #  #  #  #  
------------------------------------
#     A  #                    #  #  
------------------------------------
#        #  #     #  #  #  #  #  #  
------------------------------------
#              #              #  #  
------------------------------------
#  #  #  #     #  #     #  #     #  
------------------------------------
#              #        #     #  #  
------------------------------------
#     #  #  #  #        #     #  #  
------------------------------------
#     #              #  #     #  #  
------------------------------------
#     #  #     #  #  #  #  #     #  
------------------------------------
#              #              #  #  
------------------------------------
#  #     #           #  #     #  #  
------------------------------------
#  #  #  #  #  #  B  #  #  #  #  #  
Reached
------------------------------------
#  #  #  #  #  #  #  #  #  #  #  #  
------------------------------------
#     A  #                    #  #  
------------------------------------
#     *  #  #     #  #  #  #  #  #  
------------------------------------
#     *  *  *  #              #  #  
------------------------------------
#  #  #  #  *  #  #     #  #     #  
------------------------------------
#  *  *  *  *  #        #     #  #  
------------------------------------
#  *  #  #  #  #        #     #  #  
------------------------------------
#  *  #              #  #     #  #  
------------------------------------
#  *  #  #     #  #  #  #  #     #  
------------------------------------
#  *  *  *  *  #              #  #  
------------------------------------
#  #     #  *  *  *  #  #     #  #  
------------------------------------
#  #  #  #  #  #  B  #  #  #  #  # 
```
