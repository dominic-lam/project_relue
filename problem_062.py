import time, utilities, os, itertools
import math
import numpy

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()


    # cubic_list = []
    # i = 1
    # while True:
    #     print(i)
    #     cube = pow(i,3)
    #     cubic_list.append(cube)
    #     perms = list(itertools.permutations(str(cube)))
    #     perms = list(dict.fromkeys(perms))
    #     cubics = []
    #     for perm in perms:
    #         k = ''
    #         for j in perm:
    #             k += j
    #
    #         if int(k) in cubic_list and len(str(int(k))) == len(str(cube)):
    #             print(int(k))
    #
    #             cubics.append(k)
    #
    #     if len(cubics) == 3:
    #         print(cubics)
    #         break
    #     i+=1
    #
    # #took 7.36s to get 405^3, 3 cubes

    i = 1
    while True:
        print(i)
        cube = pow(i,3)
        perms = list(itertools.permutations(str(cube)))
        perms = list(dict.fromkeys(perms))
        cubics = []
        for perm in perms:
            k = ''

            for j in perm:
                k += j

            if (numpy.cbrt(int(k))).is_integer() and len(str(int(k))) == len(str(cube)):
                print(int(k))

                cubics.append(k)

        if len(cubics) == 5:
            print(cubics)
            break
        i+=1

    # took 3.73s to get 405^3, 3 cubes


    # i = 405
    # cube = pow(i, 3)
    # perms = list(itertools.permutations(str(cube)))
    # perms = list(dict.fromkeys(perms))
    # cubics = []
    # for perm in perms:
    #     k = ''
    #
    #     for j in perm:
    #         k += j
    #
    #     print(k)
    #
    #     if (numpy.cbrt(int(k))).is_integer() and len(str(int(k))) == len(str(cube)):
    #         print(int(k), 'hello')
    #         cubics.append(k)
    #
    # if len(cubics) == 3:
    #     print(cubics)
    #


    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
