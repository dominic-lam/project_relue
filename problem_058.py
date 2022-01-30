import time, utilities, os

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
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    side_length = 3
    prime_on_d_count = 0
    num = 1
    while True:
        #Todo
        # 1. generate the number at the corner for each side length
        # 2. count primes on diagonal

        for i in range(0,4):
            num += side_length-1
            if utilities.is_prime(num):
                prime_on_d_count += 1

        # prime_on_d_count = 0
        # for i in range(0, side_length):
        #
        #     if (A[i][i] in prime_list) or utilities.is_prime(A[i][i]):
        #         prime_on_d_count += 1
        #         if not (A[i][i] in prime_list):
        #             prime_list.append(A[i][i])
        #
        #     if (A[side_length - 1 - i][i] in prime_list) or utilities.is_prime(A[side_length - 1 - i][i]):
        #         prime_on_d_count += 1
        #         if not (A[side_length - 1 - i][i] in prime_list):
        #             prime_list.append(A[side_length - 1 - i][i])

        # if utilities.is_prime(A[0][0]):
        #     prime_on_d_count += 1
        # if utilities.is_prime(A[side_length-1][0]):
        #     prime_on_d_count += 1
        # if utilities.is_prime(A[0][side_length-1]):
        #     prime_on_d_count += 1
        # if utilities.is_prime(A[side_length-1][side_length-1]):
        #     prime_on_d_count += 1

        total_number_on_diagonal_count = 2*side_length - 1
        print(side_length, prime_on_d_count, total_number_on_diagonal_count)

        if prime_on_d_count/total_number_on_diagonal_count < 0.1:

            # print_matrix(A)
            # print(side_length, prime_on_d_count, total_prime_count)
            break

        side_length+=2



    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
