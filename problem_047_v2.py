import time, utilities, os
import ig_scraper
import pandas
import primesieve

prime_list = []

def get_prime_fators(k):
    prime_fator_list = []
    n = k
    for p in prime_list:
        if n%p == 0:
            n = n/p
            prime_fator_list.append(p)
            while n%p == 0:
                n = n/p
        if n == 1:
            break

    return prime_fator_list

def get_prime_factors_count(k):
    return len(get_prime_fators(k))

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    # prime_list = utilities.get_prime_list_under_n(10**6)
    prime_list = primesieve.primes(10**6)
    
    print('done getting prime list')

    prime_count = 4

    i = 3
    while True:
        print(i)
        if get_prime_factors_count(i) == prime_count and get_prime_factors_count(i+1) == prime_count and get_prime_factors_count(i+2) == prime_count and get_prime_factors_count(i+3) == prime_count:
            print(i)
            break
        i+=1

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
