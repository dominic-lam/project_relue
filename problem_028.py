NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0) # directions
turn_right = {NORTH: E, E: S, S: W, W: NORTH} # old -> new direction

def spiral(width, height):
    if width < 1 or height < 1:
        raise ValueError
    x, y = width // 2, height // 2 # start near the center
    dx, dy = NORTH # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count # visit
        # try to turn right
        new_dx, new_dy = turn_right[dx,dy]
        new_x, new_y = x + new_dx, y + new_dy
        if (0 <= new_x < width and 0 <= new_y < height and
            matrix[new_y][new_x] is None): # can turn right
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy
        else: # try to move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix # nowhere to go

def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = "{:0%dd}" % width
    for row in matrix:
        print(" ".join("_"*width if el is None else fmt.format(el) for el in row))


if __name__ == '__main__':
    n = 1001
    #Todo:
    # 1. generate a 1001x1001  clockwise direction spiral
    # spiral_matrix = spiral(1001,1001)
    spiral_matrix = spiral(n, n)
    # print_matrix(spiral_matrix)

    #Todo:
    # 2. calculate the sum of diagonals and minus 1 for double counting
    left_to_right_diagonal = 0
    right_to_left_diagonal = 0
    for i in range(0,n):
        # print(spiral_matrix[i][i], spiral_matrix[i][n-1-i])
        left_to_right_diagonal += spiral_matrix[i][i]
        right_to_left_diagonal += spiral_matrix[i][n-1-i]

    print(left_to_right_diagonal + right_to_left_diagonal - 1)

