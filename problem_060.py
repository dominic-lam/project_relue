import time, utilities, os, itertools

def is_remarkable_pair(a:int, b:int):
    if utilities.is_prime(int(str(a) + str(b))) and utilities.is_prime(int(str(b)+str(a))):
        return True

def is_remarkable_combination(primes:[int]):
    combinations = itertools.combinations(primes,2)
    all_remarkable = True
    for combination in combinations:
        if not is_remarkable_pair(combination[0], combination[1]):
            all_remarkable = False
            break
    return all_remarkable



if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))
    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    prime_list = [2,3]
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    # ls = [3, 7, 109, 674]
    # print(is_remarkable_combination(ls))
    # remarkable_primes_length = 2
    #
    # for i in range(5, 1000, 2):
    #     if utilities.is_prime(i):
    #         prime_list.append(i)
    # print('Finish generating prime list under 100k')
    #
    # combinations = itertools.combinations(prime_list,remarkable_primes_length)
    # results = []
    # for combination in combinations:
    #     if is_remarkable_combination(combination):
    #         print(sum(combination), combination)
    #         results.append((sum(combination), combination))

    remarkable_primes_length = 5
    i = 5

    remarkable_primes_combinations = []

    while True:

        if utilities.is_prime(i):
            # Check if all smaller primes are remarkable to i
            for j in range(len(prime_list)-1, -1,-1):
                if is_remarkable_pair(prime_list[j], i):
                    remarkable_primes_combinations.append([i,prime_list[j]])

            for combination in remarkable_primes_combinations:
                if is_remarkable_combination(combination + [i]):
                    remarkable_primes_combinations.append(combination + [i])
                    if len(combination + [i]) == remarkable_primes_length - 1:
                        print(combination + [i])

                    if len(combination + [i]) == remarkable_primes_length:
                        print(sum(combination + [i]), combination + [i])
                        exit()

            # print(i, remarkable_primes_combinations)
            prime_list.append(i)
        i += 2


    # while True:
    #     print(i)
    #     remarkable_primes = []
    #     if utilities.is_prime(i):
    #         remarkable_primes.append(i)
    #         prime_list.append(i)
    #
    #         #Check if all smaller primes are remarkable to i
    #         for j in range(0, len(prime_list)-1):
    #             if is_remarkable_pair(prime_list[j], i):
    #                 remarkable_primes.append(prime_list[j])
    #
    #         if len(remarkable_primes) >= remarkable_primes_length:
    #             #Check if all primes in the list are remarkable to each other
    #             combinations = list(itertools.combinations(remarkable_primes,2))
    #             they_are_all_remarkable = True
    #             for combination in combinations:
    #                 if not is_remarkable_pair(combination[0],combination[1]):
    #                     they_are_all_remarkable = False
    #                     break
    #
    #             if they_are_all_remarkable:
    #                 print(remarkable_primes)
    #
    #
    #     i+=2
    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
