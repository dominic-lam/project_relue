import time, utilities, os
import math
import concurrent.futures

def find_the_minimal_x_for_pell_equation_with_d(d:int):
    i = 1
    while True:
        x = math.sqrt(1+d*i*i)
        if x.is_integer():
            print('(x,d,y):',x,d,i)
            return (x,d,i)

        i += 1


if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()


    max_x = 0
    max_d = 0

    ls = []
    for d in range(1, 1000+1):
        if not math.sqrt(d).is_integer():
            ls.append(d)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(find_the_minimal_x_for_pell_equation_with_d, ls)

        for (x,D,y) in results:
            if x > max_x:
                max_x = x
                max_d = D


    print(max_x, max_d)

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))