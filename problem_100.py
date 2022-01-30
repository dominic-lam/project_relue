import time, utilities, os
import math
from fractions import Fraction

def check_if_n_qulified(n):
    # print(n)
    delta = math.sqrt(1+2*n*(n-1))
    x = (1+delta)/2
    if x.is_integer():
        x = int(x)
        a = (x*(x-1))
        b = (n*(n-1))

        if 2*a == b:
            print('B: ', x, ', R:', n - x, ', P(BB):', Fraction(a, b))
            return True

    return False

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    i = int(math.pow(10,12))
    # while True:
    while True: #i < 10000:
        if check_if_n_qulified(i):
            break
        i+=1




    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
