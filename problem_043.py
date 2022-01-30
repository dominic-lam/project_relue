import time, utilities, os
import math
import concurrent.futures

prime_list = [2, 3, 5, 7, 11, 13, 17]

def get_sub_string_divisible_by_primes():
    sub_strings_list = []

    for p in prime_list:
        sub_strings = []
        i = 1
        while True:
            if p*i >= 1000:
                break

            temp_sub_string = ''

            if 10 <= p*i and p*i < 100:
                temp_sub_string = '0' + str(p*i)

            if 100 <= p*i and p*i < 1000:
                temp_sub_string = str(p*i)

            if not utilities.checkIfDuplicates_1(temp_sub_string) and temp_sub_string != '':
                sub_strings.append(temp_sub_string)

            i += 1

        sub_strings_list.append(sub_strings)
    return sub_strings_list

def generate_target_combinations():
    sub_strings_list = get_sub_string_divisible_by_primes()
    combinations = []

    for d1 in sub_strings_list[0]:
        for d2 in sub_strings_list[1]:
            if (d1[-2] + d1[-1]) == d2[0] + d2[1] and not utilities.checkIfDuplicates_1(d1 + d2[2]):
                for d3 in sub_strings_list[2]:
                    if (d2[-2] + d2[-1]) == d3[0] + d3[1] and not utilities.checkIfDuplicates_1(d1 + d2[2] + d3[2]):
                        for d4 in sub_strings_list[3]:
                            if (d3[-2] + d3[-1]) == d4[0] + d4[1] and not utilities.checkIfDuplicates_1(d1 + d2[2] + d3[2] + d4[2]):
                                for d5 in sub_strings_list[4]:
                                    if (d4[-2] + d4[-1]) == d5[0] + d5[1] and not utilities.checkIfDuplicates_1(
                                        d1 + d2[2] + d3[2] + d4[2] + d5[2]):
                                        for d6 in sub_strings_list[5]:
                                            if (d5[-2] + d5[-1]) == d6[0] + d6[1] and not utilities.checkIfDuplicates_1(
                                                    d1 + d2[2] + d3[2] + d4[2] + d5[2] + d6[2]):
                                                for d7 in sub_strings_list[6]:
                                                    if (d6[-2] + d6[-1]) == d7[0] + d7[
                                                        1] and not utilities.checkIfDuplicates_1(
                                                            d1 + d2[2] + d3[2] + d4[2] + d5[2] + d6[2] + d7[2]):
                                                        combination = d1 + d2[2] + d3[2] + d4[2] + d5[2] + d6[2] + d7[2]
                                                        for i in range(0,10):
                                                            k = str(i) + combination
                                                            if not utilities.checkIfDuplicates_1(k):
                                                                combinations.append(k)
                                                                print(k)
    return combinations

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))
    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()
    sum_of_targets = 0 #The targets are all 0-9 pandigital number and sub-string divisible
    sum = 0

    for c in generate_target_combinations():
        sum += int(c)



    print('Sum:', sum)
    print("---Time Spent:  %s seconds ---" % (time.time() - start_time))




# def check_sub_string_divisible_by_primes(i):
#
#
#     s = str(i)
#     sub_strings = []
#     for i in range(1,8):
#         sub_string = int(s[i+0] + s[i+1] + s[i+2])
#         sub_strings.append(sub_string)
#
#     all_divisible = True
#     for j in range(0, len(prime_list)):
#         d = sub_strings[j]
#         p = prime_list[j]
#         if not d%p == 0:
#             return False
#         # else:
#         #     print(d, 'is divisible by', p)
#
#     print(i, 'is a 0-9 pandigital number and sub-string divisible')
#     return True
#
# def main(i):
#     s = str(i)
#     if utilities.check_if_0_to_9_pandigital(s):
#         print(s, 'is 0 to 9 pandigital')
#         if check_sub_string_divisible_by_primes(i):
#             return i
#     return 0
#
# if __name__ == '__main__':
#     problem_number_str = utilities.get_problem_number(os.path.basename(__file__))
#     print('Start working on Project Euler Problem: ' + problem_number_str)
#     start_time = time.time()
#
#     start_index = int(math.pow(10,9))
#     end_index = int(math.pow(10,10))
#
#     # main(1406357289)
#
#     sum = 0
#
#     for i in range(start_index, end_index):
#         sum += main(i)
#
#     # Todo: let's try multiprocessing method
#     # ls = list(range(start_index, end_index))
#     # with concurrent.futures.ProcessPoolExecutor() as executor:
#     #     results = executor.map(main, ls)
#     #
#     #     for result in results:
#     #         sum += result
#
#     print(sum)
#     print("---Time Spent:  %s seconds ---" % (time.time() - start_time))