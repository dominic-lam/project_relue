import time, utilities, os

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    limit = 50
    y_limit = ()
    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
