import time, utilities, os
from decimal import *

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    getcontext().prec = 100

    sum = 0
    for i in range(1,101):
        if not pow(i,0.5).is_integer():

            decimal_part = (str(Decimal(i).sqrt())).split('.')[1]

            i_sum = 0
            for d in decimal_part:
                i_sum += int(d)

            print(i, decimal_part,i_sum)

            sum += i_sum
    print(sum)

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
