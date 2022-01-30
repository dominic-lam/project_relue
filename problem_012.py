import concurrent.futures
import time, utilities, os


def get_divisors(n):
    divisors = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return divisors

def compute_triangular_number_and_check_divisors_count(n):
    n_th_triangular_number = n*(n+1)/2
    divisors = get_divisors(n_th_triangular_number)
    # print(str(n) + '-th:', n_th_triangular_number, len(divisors), divisors)
    if len(divisors) > 500:
        print(str(n) + '-th:', n_th_triangular_number, len(divisors), divisors)

def gen_prime_list(n_terms = 10000):
    prime_list = [2]
    i = 3
    while len(prime_list) < n_terms + 1:
        is_prime = True
        for j in prime_list:
            if i % j == 0 and j != 1:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
            # print(len(prime_list), i)
        i += 2
    return prime_list


if __name__ == '__main__':
    # #Method 1 Single Processor, the slow way
    # i = 1
    # max_divisors_count = 0
    # max_divisors_triangular_number = 0
    # max_divisors = []
    # triangle_number = 0
    #
    # while True:
    #
    #     triangle_number += i
    #     divisors = get_divisors(triangle_number)
    #     if len(divisors) > max_divisors_count:
    #         max_divisors_count = len(divisors)
    #         max_divisors_triangular_number = triangle_number
    #         print(str(i)+'-th triangular number:', triangle_number, max_divisors_count, divisors)
    #
    #     if len(divisors)>500:
    #         print(triangle_number)
    #         exit()
    #     i += 1

    # #Method2 The multiprocessor, brute force
    # #It took a lot of time for Method 1 to find the number, I can't even wait for the answer
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     ls = list(range(1000000))
    #     results = executor.map(compute_triangular_number_and_check_divisors_count, ls)
    #


    #Method 3 Fast way
    #build a prime list by problem 007 and get d(n)
    #Ans = 12375-th Triangular Number: 76576500
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()
    prime_list = gen_prime_list()
    i = 3
    divisors_count = 500
    while True:
        n = i*(i+1)/2
        nth_tri = n
        divisors_power = []
        for p in prime_list:
            if p > pow(nth_tri, 0.5) + 1:
                break
            power = 0
            if n % p == 0:
                is_prime = False
                while n % p == 0:
                    n = n / p
                    power += 1
                divisors_power.append(power)
                if n == 1:
                    break

        count = 1
        for e in divisors_power:
            count *= (e+1)
        if count >= divisors_count:
            print(i,int(nth_tri), count)
            break

        i += 1

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
