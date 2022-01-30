import time, utilities, os
from fractions import Fraction

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    reversed_fraction_list = []

    for i in range(33,0,-1):
        reversed_fraction_list.append(1)
        reversed_fraction_list.append(2*i)
        reversed_fraction_list.append(1)

    print(len(reversed_fraction_list),reversed_fraction_list)

    e = 0

    for f in reversed_fraction_list:
        e = Fraction(1, Fraction(f+e))

    e = 2 + e

    print(e)
    numberator = e.numerator
    sum = 0
    for x in str(numberator):
        sum += int(x)
    print(sum)
    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
