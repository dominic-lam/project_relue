import time, utilities, os


if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()
    limit = 1000000
    # limit = 10

    #Smart Way
    #Todo, Explain
    i = 3
    ans = 2
    while True:
        if utilities.is_prime(i):
            if ans*i > limit:
                break
            else:
                ans *= i
        i+=2

    print(ans)

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
