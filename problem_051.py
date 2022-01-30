import time, utilities, os
from itertools import combinations

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    prime_list = [2,3,5,7,11,13,17,19]

    #Notes:
    #1. The target number we looking must be ended with 1,3,7,9
    #2. Must have 3 digits repeating, by digit sum mod 3 observation
    #3. Must be at least 5 digits, 6 digits is also possible

    #Tatics
    #First we start with 5 digits, then 6 digits
    #Gen Combinations of the repeating digits locaiton, if 0 (the first digit) is in the combination,
    #we don't try 0
    #Now we 3 repeating digits and 1 ending digit, we have to gen all the other 2 digits possibilites for each combination

    list_5 = [0,1,2,3]
    list_6 = [0,1,2,3,4]
    ending_digit = [1,3,7,9]

    # five_digit_combinations = list(combinations(list_5,3))
    #
    # for five_digit_combination in five_digit_combinations:
    #     temp_comb = list(five_digit_combination)
    #     repeating_start_digit = 1 if 0 in temp_comb else 0
    #     rest_digit_location = list(set(list_5)-set(five_digit_combination))
    #     rest_start_digit = 1 if 0 in rest_digit_location else 0
    #     for e in ending_digit:
    #         for i in range(rest_start_digit,10):
    #             prime_list = []
    #             for r in range(repeating_start_digit, 10):
    #                 gen_num_str_list = [None]*5
    #                 gen_num_str_list[4] = e
    #                 gen_num_str_list[rest_digit_location[0]] = i
    #                 for location in temp_comb:
    #                     gen_num_str_list[location] = r
    #
    #                 gen_num_str = ''
    #                 for x in gen_num_str_list:
    #                     gen_num_str += str(x)
    #                 gen_num = int(gen_num_str)
    #
    #                 if utilities.is_prime(gen_num):
    #                     prime_list.append(gen_num)
    #
    #             if len(prime_list) >= 5:
    #                 print(prime_list)
    # #So we knew that the target is not a 5 digit number

    six_digit_combinations = list(combinations(list_6, 3))

    for six_digit_combination in six_digit_combinations:
        temp_comb = list(six_digit_combination)
        repeating_start_digit = 1 if 0 in temp_comb else 0
        rest_digit_location = list(set(list_6) - set(six_digit_combination))
        rest_start_digit = 10 if 0 in rest_digit_location else 0
        for e in ending_digit:
            for i in range(rest_start_digit, 100):
                prime_list = []
                for r in range(repeating_start_digit, 10):
                    gen_num_str_list = [None] * 6
                    gen_num_str_list[5] = e
                    if i < 10:
                        gen_num_str_list[rest_digit_location[0]] = 0
                        gen_num_str_list[rest_digit_location[1]] = int(str(i)[0])
                    else:
                        gen_num_str_list[rest_digit_location[0]] = int(str(i)[0])
                        gen_num_str_list[rest_digit_location[1]] = int(str(i)[1])
                    for location in temp_comb:
                        gen_num_str_list[location] = r

                    gen_num_str = ''
                    for x in gen_num_str_list:
                        gen_num_str += str(x)
                    gen_num = int(gen_num_str)

                    if utilities.is_prime(gen_num):
                        prime_list.append(gen_num)

                if len(prime_list) >= 8:
                    print(prime_list)



    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
    # [121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
    # ---Time spent: 0.21875476837158203 seconds ---