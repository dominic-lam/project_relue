import time, utilities, os

prime_list = [2,3,5]

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()
    limit = 1000000

    #Todo: Step 1 Gen all primes under 1 Million
    for i in range(7,limit+1,2):
        if utilities.is_prime(i):
            prime_list.append(i)

    print(prime_list)
    print('Total Number of Primes <',limit,':',len(prime_list))

    j = 1
    prime_sum = 0
    while prime_sum < prime_list[-1]:
        prime_sum += prime_list[j]
        j += 1

    if prime_sum in prime_list:
        print(prime_sum, j)
        exit()
    print('No primes can be written as sum of '+str(j)+' conescutive primes')
    consecutive_primes_count = j-1
    while True:
        print('===============================================')
        print('Checking for consecutive_primes_count =', consecutive_primes_count)
        print('j:',j)
        for x in range(0, j - consecutive_primes_count + 1):
            sub_prime_sum = 0
            print('let sum primes in list from',x,'th term to', x + consecutive_primes_count - 1,'th term')
            for y in range(x, x+consecutive_primes_count ):
                sub_prime_sum += prime_list[y]
            print('sum: ', sub_prime_sum)

            if sub_prime_sum in prime_list:
                print('Target found')
                print(sub_prime_sum, consecutive_primes_count, 'terms, start from',x,'-th term')
                exit()

        print('No primes can be written as sum of ' + str(consecutive_primes_count) + ' conescutive primes')
        consecutive_primes_count -= 1



    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
