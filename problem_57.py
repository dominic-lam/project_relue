import time, utilities, os
from fractions import Fraction
if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    # i = 1
    # while i < 4:
    #     i += 1
    #     k = 1/2
    #     for j in range(1, i+1):
    #         k = 1/(2+k)
    #     f = 1 + k
    #     print(i, Fraction(f))
    #

    # i = 2
    # k = 1/2
    #
    # for j in range(0,i):
    #     k = 1/(2+k)
    #     print(j+1, k)
    # f = (1+k)
    # print(f, Fraction(f).limit_denominator())

    k_list = [Fraction(1,2)]

    for k in range(1,1000):
        k_list.append(Fraction(1,( k_list[-1] + 2)))

    f_list = [i+1 for i in k_list]

    count = 0
    for f_ in f_list:
        if len(str(f_.numerator)) > len(str(f_.denominator)):
            count += 1
            print(f_)
    print(count)

    # for i in range(0, len(f_list)):
    #     print(i+1, Fraction(str(f_list[i])))


    # i = 2, f = 7/5

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
