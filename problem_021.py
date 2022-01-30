import utilities, time, os

#Method 1
def get_proper_divisors(n):
    divisors = []
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

#Method 1
def sum_of_list(list:[int]):
    sum = 0
    for i in list:
        sum += i
    return sum

#Method 2: get sum of proper divisors with prime factorization
def sum_of_proper_divisors(k:int, prime_list:[int]):
    sigma = 1
    n = k
    if k in prime_list:
        return 1

    for p in prime_list:
        if p > k/2:
            break
        if n%p == 0:

            e = 1
            n = n/p
            while n%p == 0:
                e += 1
                n = n/p
            sigma *= (pow(p,e+1)-1)/(p-1)

    return int(sigma - k)

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    # #Method 1
    # ans = 0
    # for i in range(2, 10000):
    #     divisors = get_proper_divisors(i)
    #     sum_of_divisor = sum_of_list(divisors)
    #     if sum_of_list(get_proper_divisors(sum_of_divisor)) == i and sum_of_divisor != i:
    #         print(i, sum_of_divisor)
    #         ans += i
    # print(ans)
    # # ...with some result in advanced
    # # 31626
    # # ---Time spent:  1.2753758430480957 seconds ---

    #Method 2, using prime factorization to find the sum of proper divisors
    prime_list = utilities.get_prime_list_under_n(10000)
    print(sum_of_proper_divisors(2,prime_list))

    ans = 0
    for i in range(2, 10000):
        a = i
        b = sum_of_proper_divisors(a,prime_list)

        if a == sum_of_proper_divisors(b,prime_list) and b!=a:
            print(a, b)
            ans += i
    print(ans)
    # ...with some result in advanced
    # 31626
    # ---Time spent:  0.7922632694244385 seconds ---


    print("---Time spent:  %s seconds ---" % (time.time() - start_time))

