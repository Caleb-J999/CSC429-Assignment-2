
#0 = open cell
#1 = blocked cell
grid = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 0, 0, 1, 1],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 1, 1]
]


# Starting point A
start = (6, 0)

# Goal B
goal = (3, 3)

moves = [
    (-1, 0),   # Up
    (0, 1),    # Right
    (1, 0),    # Down
    (0, -1)    # Left
]


# neighboring cells
def get_neighbors(grid, cell):

    row, col = cell

    neighbors = []

    for row_change, col_change in moves:

        new_row = row + row_change
        new_col = col + col_change

        
        if (
            0 <= new_row < len(grid)
            and
            0 <= new_col < len(grid[0])
        ):

            if grid[new_row][new_col] == 0:

                neighbors.append((new_row, new_col))

    return neighbors


#DLS 
def depth_limited_search(grid, start, goal, limit):

    path = [start]

    examined = []

    expanded = []


    def recursive_dls(current, depth):

        examined.append(current)

        if current == goal:
            return path.copy()



        if depth == limit:
            return None


        expanded.append(current)


        for neighbor in get_neighbors(grid, current):

        
            if neighbor not in path:

                path.append(neighbor)

                result = recursive_dls(neighbor, depth + 1)

                if result is not None:
                    return result

                path.pop()


        return None


    result = recursive_dls(
        start,
        0
    )


    return result, examined, expanded

#RUN DLS WITH LIMIT = 6
path_6, examined_6, expanded_6 = depth_limited_search(
    grid,
    start,
    goal,
    6
)


print("================================")
print("DLS WITH DEPTH LIMIT = 6")
print("================================")


if path_6 is not None:

    print("Goal found!")

    print("\nPath:")

    for node in path_6: print(node)

    print("\nPath length:",len(path_6) - 1,"moves")

else:

    print("Goal was not found.")


print("\nNodes examined:")
print(examined_6)

print("\nNumber of nodes examined:",len(examined_6))

print("Number of nodes expanded:",len(expanded_6))


#RUN DLS WITH LIMIT = 10
path_10, examined_10, expanded_10 = depth_limited_search(
    grid,
    start,
    goal,
    10
)


print("\n================================")
print("DLS WITH DEPTH LIMIT = 10")
print("================================")


if path_10 is not None:

    print("Goal found!")

    print("\nPath:")

    for node in path_10:
        print(node)

    print("\nPath length:", len(path_10) - 1, "moves")

else:

    print("Goal was not found.")


print("\nNodes examined:")
print(examined_10)

print(
    "\nNumber of nodes examined:", len(examined_10)
)

print(
    "Number of nodes expanded:", len(expanded_10)
)