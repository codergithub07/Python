# This problem is solved using the backtracking algorithm

# initializing the maze with all blocked paths
mazeSize = int(input("Enter Maze size: "))
maze = [[0 for _ in range(mazeSize)] for _ in range(mazeSize)]
solMaze = [[0 for _ in range(mazeSize)] for _ in range(mazeSize)]
solMaze[0][0] = 1

def printSolMaze(solMaze: list[list]):
    for row in solMaze:
        print(row)
    print()  # For better readability between steps

# Creating Maze
print(f"Make your own path in the maze from (0, 0) to ({mazeSize-1}, {mazeSize-1})")
maze[0][0] = 1
a, b = 0, 0
while a != mazeSize-1 or b != mazeSize-1:
    for row in maze:
        print(row)
    a, b = map(int, input("Enter the coordinates (x, y): "))
    maze[a][b] = 1
for row in maze:
    print(row)

# Maze working:
def safePlace(maze: list[list], x: int, y: int, mazeSize: int):
    if 0 <= x < mazeSize and 0 <= y < mazeSize and maze[x][y] == 1:
        return True
    return False

def moveRat(maze: list[list], x: int, y: int, solMaze: list[list], mazeSize: int):

    # Base case: if the rat has reached the destination
    if x == mazeSize - 1 and y == mazeSize - 1:
        solMaze[x][y] = 1
        printSolMaze(solMaze)
        print("Reached the destination!")
        return True
    
    if safePlace(maze, x, y, mazeSize):
        # Mark x, y as part of the solution path
        solMaze[x][y] = 1
        printSolMaze(solMaze)
        
        # Try moving Down
        if moveRat(maze, x + 1, y, solMaze, mazeSize):
            return True
        
        # Try moving Right
        if moveRat(maze, x, y + 1, solMaze, mazeSize):
            return True
        
        # If neither down nor right worked, backtrack: unmark x, y as part of the solution path
        solMaze[x][y] = 0
        print(f"Backtracking from ({x}, {y})")
        printSolMaze(solMaze)  # Print the maze after backtracking
        return False

    return False

print()
if not moveRat(maze, 0, 0, solMaze, mazeSize):
    print("No solution found.")