import time, utilities, os

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()
    n_digit_integer_list = []
    i = 1
    while True:
        n_digit_integer_list.append([])
        j = 1
        while True:
            if len(str(j ** i)) == i:
                n_digit_integer_list[i-1].append(j)
            if len(str(j**i)) > i:
                break
            j+=1

        print(i, n_digit_integer_list[i-1], len(n_digit_integer_list[i-1]))

        if len(n_digit_integer_list[i-1]) == 0:
            break
        i+=1

    count = 0
    for list in n_digit_integer_list:
        count += len(list)
    print(count)

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
