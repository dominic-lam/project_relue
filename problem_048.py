import time, utilities, os, math

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    b = pow(10,10)

    sum = 0
    for i in range(1, 1000+1):
        sum += pow(i,i,b)

    print(sum%b)


    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
