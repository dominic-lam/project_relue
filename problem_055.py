import time, utilities, os

def check_if_palindromic(n:int):
    a = str(n)
    b = a[::-1]
    return a==b

def get_reverse_and_add(n:int):
    b = str(n)[::-1]
    return n+int(b)

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    i = 1
    lychrel_number_count = 0
    while i < 10000:
        num = i
        is_lychrel = True
        for j in range(1, 50):
            if check_if_palindromic(get_reverse_and_add(num)):
                #j in here is the number of steps required for num to be check_if_palindromic
                is_lychrel = False
                break
            else:

                num = get_reverse_and_add(num)
        if is_lychrel:
            print(i)
            lychrel_number_count += 1
        i+=1

    print(lychrel_number_count)

    # i = 196
    # is_lychrel = True
    # num = i
    # for j in range(1, 16):
    #     if check_if_palindromic(get_reverse_and_add(num)):
    #         #j in here is the number of steps required for num to be check_if_palindromic
    #         print(j, str(num), '+', str(num)[::-1], '=', get_reverse_and_add(num))
    #         print(i, 'is palindromic')
    #         is_lychrel = False
    #         break
    #     else:
    #         print(j, str(num), '+', str(num)[::-1],'=',get_reverse_and_add(num))
    #         num = get_reverse_and_add(num)
    #
    # if is_lychrel:
    #     print(i, 'is Lychrel')



    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
