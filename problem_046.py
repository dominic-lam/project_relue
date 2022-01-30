import time, utilities, os

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    prime_list = [2,3,5,7]

    i = 9
    while True:
        if utilities.is_prime(i):
            prime_list.append(i)
        else:


            j = 1
            conjecture_holds = False
            while 2*(j**2) < i:
                twice_a_square = 2*(j**2)

                if (i - twice_a_square) in prime_list:

                    conjecture_holds = True
                    print(i,'=',(i - twice_a_square),'+ 2*'+str(j)+'^2')
                    break
                j+=1
            if not conjecture_holds:
                print(i)
                break

        i+=2


    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
