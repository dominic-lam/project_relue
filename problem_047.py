import time, utilities, os

prime_list = [2]

def get_prime_factor_list(n:int):
    prime_factors = []
    if n%2 == 0:
        prime_factors.append(2)

    for i in range(3, int(n**1/2) + 1, 2):

        if n%i == 0 and utilities.is_prime(i):
            prime_factors.append(i)
    return prime_factors

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    prime_count = 4

    i = 3
    while True:
        print(i)
        if len(get_prime_factor_list(i)) == prime_count:
            if len(get_prime_factor_list(i+1)) == prime_count:
                if len(get_prime_factor_list(i+2)) == prime_count:
                    if len(get_prime_factor_list(i+3)) == prime_count:
                        print(i, get_prime_factor_list(i))
                        print(i+1, get_prime_factor_list(i+1))
                        print(i+2, get_prime_factor_list(i+2))
                        print(i+3, get_prime_factor_list(i+3))
                        break
        i+=1

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))