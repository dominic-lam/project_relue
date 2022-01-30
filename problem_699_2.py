import time, utilities, os,math
from fractions import Fraction

prime_list = []

def check_is_power_of_3(denomiator):
    k = math.log(denomiator,3)
    return k.is_integer() and k > 0

def sub_big_t(n:int):
    if n%3 != 0:
        return 0
    else:
        sigma_n = utilities.sigma(n, prime_list)
        f = Fraction(sigma_n,n)

        if check_is_power_of_3(f.denominator):
            print('sigma(n):',sigma_n, ', n:',n, 'Lowest a/b:',f)
            return n
        return 0

if __name__ == '__main__':
    #still too slow, not to say T(10^6) is not correct, answer of thie solution is 19438302, where the ans given on the website is 26089287
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()


    limit = pow(10,2)
    prime_list = utilities.get_prime_list_under_n_with_primesieve(limit)
    big_t = 0
    for i in range(1,limit+1):
        big_t += sub_big_t(i)
    print(big_t)
    #

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))