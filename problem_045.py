import time, utilities, os, math

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    i = 2
    k = 0
    while True:
        h_n = utilities.generate_nth_hexagonal_number(i)
        if utilities.is_pentagonal(h_n) and utilities.is_triangle_number(h_n) :
            print(h_n, 'is triangle, pentagonal and hexagonal')
            k += 1
            if k == 2:
                break
        i += 1


    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
