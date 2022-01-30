import time, utilities, os

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    #Find the sum of all the multiples of 3 or 5 below 1000.
    # for i in range(3,1000):
    #     if i%3 == 0 or i%5 ==0:
    #         sum += i
    limit = 1000
    l = list(i for i in range(1,limit) if (i%3 == 0 or i%5 ==0))
    print(sum(l))


    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
