import time, utilities, os
import itertools

def is_permuation_indentical(a,b):
    return sorted(str(a)) == sorted(str(b))


if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    # n = 87109
    # phi_n = utilities.phi(n)
    # print(n, phi_n, is_permuation_indentical(n, phi_n))
    # 87109 79180 True

    #Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
    #Note that to minimized the ratio, find smallest n s.t. n, phi(n) are permuation identical
    limit = 10**7
    i = limit-1
    while True:
        if utilities.is_prime(i):
            print(i)
            phi_i = utilities.phi(i)
            if is_permuation_indentical(i, phi_i):
                print(i, phi_i, i / phi_i)
        i -= 1



    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
