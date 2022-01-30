import time, utilities, os
from fractions import Fraction
if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()
    limit = 8
    # #First let's gen the example set of proper fractions
    # limit = 1000000
    # fraction_list = []
    # for i in range(1, limit+1):
    #     for j in range(1,i):
    #         f = Fraction(j, i)
    #         if not f in fraction_list:
    #             fraction_list.append(f)
    #
    # for item in sorted(fraction_list):
    #     print(item)

    limit = 1000000


    #Find a,b s.t. a/1000000 < 3/7 < b/1000000 and b = a + 1, a = 428570, b = 428571
    # for i in range(limit+1):
    #     if i/limit < 3/7 and (i+1)/limit:
    #         print(i)
    a = 428570
    b = 428571

    fraction_list = []

    lower_bound = 3/7

    limit = 12000

    for i in range(1,limit+1):
        print(i)
        for j in range(int(i*1/3),int(i*1/2)+1):
            # print('j: ', j)
            if Fraction(j,i) in fraction_list:
                continue
            if 1/3 < j/i and j/i < 1/2:
                fraction_list.append(Fraction(j,i))

    fraction_list = sorted(fraction_list)
    print(fraction_list)
    print(len(fraction_list))
    # for item in fraction_list:
    #     print(item)

    #For 3/7 = 0.42857.., we know that this is bounded by 428000/1000000 and 429000/1000000
    #So all we have
    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
