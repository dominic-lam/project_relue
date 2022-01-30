import time, utilities, os
import concurrent.futures

def get_prime_factors_of_n(n):
    prime_factor_of_n = []
    if n % 2 == 0:
        prime_factor_of_n.append(2)
    for i in range(3, int(n / 2) + 1, 2):
        if utilities.is_prime(i) and n % i == 0:
            prime_factor_of_n.append(i)

    return i, prime_factor_of_n

def phi(n):

    if n == 2:
        return 1

    prime_factors = get_prime_factors_of_n(n)
    non_relatively_prime_number = []
    for p in prime_factors:
        # print(p)
        i = 1
        while p*i < n:
            if (not p*i in non_relatively_prime_number):
                non_relatively_prime_number.append(p*i)
            i+=1

    non_relatively_prime_number.append(n)
    phi_n = n - len(non_relatively_prime_number)
    # print(n,'phi:',phi_n, non_relatively_prime_number)
    return phi_n

if __name__ == '__main__':
    start_time = time.time()
    # print(utilities.get_prime_fators(600851475143))

    # print(utilities.get_prime_list_under_n(10**6))                #---Time spent:  2.1973822116851807 seconds ---
    # print(utilities.get_prime_list_under_n_with_primesieve(10**6))  #---Time spent:  0.01868462562561035 seconds ---
    utilities.get_prime_list_under_n_with_primesieve(10 ** 14)

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
