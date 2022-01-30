import time, utilities, os
import math


if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    threshold = 1000000
    count = 0
    for i in range(0,100+1):
        for j in range(0,i+1):
            if math.comb(i,j)>threshold:
                count += 1
    print(count)

    # threshold = 1000000
    # upper_n = 0
    # lower_n = 100
    # upper_n_row_count = 0
    # lower_n_row_count = 0
    #
    # for i in range(lower_n,1,-1):
    #     if math.comb(i, int(i/2)) > threshold and math.comb(i-1, int((i-1)/2)) < threshold :
    #         upper_n = i
    #         print('upper_n: ', 23)
    #         break
    #
    # for k in range(0,upper_n+1):
    #     if math.comb(upper_n,k) > threshold:
    #         upper_n_row_count += 1
    #
    # for j in range(0, lower_n+1):
    #     if math.comb(lower_n,j) > threshold:
    #         print(lower_n,j,math.comb(lower_n,j))
    #         lower_n_row_count += 1
    #
    # ans = (upper_n_row_count + lower_n_row_count)*(lower_n - upper_n + 1)/2
    # print(ans, upper_n, lower_n, upper_n_row_count, lower_n_row_count)


    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
