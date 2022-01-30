import math
import time
import multiprocessing
import utilities
import concurrent.futures
from fractions import Fraction

prime_list = [2]

def new_sigma(n:int):
    # Sum of all divisors
    # First we find all the prime factorization of n
    prime_factor_and_power_list = []
    sigma_n = 0

    if n % 2 == 0:
        power_of_2 = 1
        while True:
            if (n % (math.pow(2, power_of_2 + 1)) != 0):
                break
            else:
                power_of_2 += 1
        prime_factor_and_power_list.append((2, power_of_2))

    for i in range(3, n + 1, 2):
        # we may start from 3 and skip or even numbers
        i_is_prime = False

        if i in prime_list:
            i_is_prime = True
        else:
            if utilities.is_prime(i):
                i_is_prime = True
                prime_list.append(i)

        if i_is_prime and n % i == 0:
            power_of_i = 1
            while True:
                if (n % (math.pow(i, power_of_i + 1)) != 0):
                    break
                else:
                    power_of_i += 1
            prime_factor_and_power_list.append((i, power_of_i))

        product = 1
        for (p, e) in prime_factor_and_power_list:
            product *= math.pow(p, e)
        if product == n:
            # print(product, prime_factor_and_power_list)
            break

    sigma_n = 1
    for (p, e) in prime_factor_and_power_list:
        sigma_n *= (math.pow(p, e + 1) - 1) / (p - 1)

    sigma_n = int(sigma_n)
    return sigma_n

def sigma(n:int):
    sigma_n = 0
    for i in range(1,n+1):
        if (n%i == 0):
            sigma_n += i
    return sigma_n

def check_is_power_of_3(denomiator):
    k = math.log(denomiator,3)
    return k.is_integer() and k > 0

def sub_big_t(n:int):
    if n%3 != 0:
        return 0

    sigma_n = sigma(n)
    f = Fraction(sigma_n, n)
    if check_is_power_of_3(f.denominator):
        print('sigma(n):',sigma_n, ', n:',n, 'Lowest a/b:',f)
        return n
    return 0

if __name__ == '__main__':


    start_time = time.time()
    sum = 0
    big_N = int(math.pow(10,6))
    #Todo: Calculating Process



    # # #Method 1 Single Processor
    # # #Note, with printing log, it took about
    # # # 0.5s for T(10^4) = 100434,
    # # # 56s for T(10^5) = 1273587
    for i in range(3, big_N+1, 3):
        sum += sub_big_t(i)

    # #Method 2 Multi Processor
    # # Note, with printing log, it took about
    # # 2.9s for T(10000) = 100434,
    # # 26s for T(10^5) = 1273587
    # # 553s for T(10^6) = 21364638? (26089287)
    # ls = list(range(1, big_N+1))
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     results = executor.map(sub_big_t, ls)
    #
    #     for result in results:
    #         sum += result
    #
    #
    print(sum)
    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
