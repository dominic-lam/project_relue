import time, utilities, os
from itertools import permutations

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    #Todo:
    # Step 1 Gen 4 digits prime list
    # Step 2 check if other permuations of a prime are also prime
    # Step 3 sort them check if they are arithmetic
    perms_of_prime_list = []
    for i in range(1000, 10000 + 1):

        if utilities.is_prime(i): #and not utilities.checkIfDuplicates_1(str(i))
            s = str(i)
            perms = [''.join(p) for p in permutations(s)]
            all_prime = True
            prime_list = []
            for i in perms:
                p = int(i)
                if utilities.is_prime(p) and p >= 1000 and not p in prime_list:
                    prime_list.append(p)

            prime_list = sorted(prime_list)
            if len(prime_list) >= 3 and prime_list not in perms_of_prime_list:
                print(prime_list)
                perms_of_prime_list.append(prime_list)


    for perms in perms_of_prime_list:
        for i in range(1,len(perms)):
            for j in range(0,i):
                mid = int((perms[i] - perms[j])/2 + perms[j])
                if mid in perms:
                    print(perms[j], mid, perms[i])


    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
