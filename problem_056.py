import time, utilities, os, math

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    max_digital_sum = 0
    max_i = 0
    max_j = 0
    max_digital_sum_result = 0

    for i in range(1,100):
        for j in range(1,100):
            digital_sum = utilities.get_digital_sum(int(pow(i,j)))
            if digital_sum > max_digital_sum:
                max_digital_sum = digital_sum
                max_j = j
                max_i = i
                max_digital_sum_result = int(i**j)

    print(max_digital_sum, max_i, max_j, max_digital_sum_result)


    # Just a little bit faster for this problem
    # max_digital_sum = max(utilities.get_digital_sum(i**j) for i in range(1,100) for j in range(1,100))
    # print(max_digital_sum)

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
