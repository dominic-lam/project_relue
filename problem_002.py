import time, utilities, os

def old_method():
    a = 1
    b = 1
    sum = 0
    while b < 4000000:
        a, b = b, a+b
        if b%2 == 0:
            sum += b
    print(sum)

def fib(max = 10):
    a = 1
    b = 1
    while a < max:
        yield a
        a,b = b, a+b


if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    #By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

    # old_method()

    # print(sum(i for i in fib(4000000) if i%2 == 0))
    print(list(i for i in fib(100)))
    print("---Time spent:  %s seconds ---" % (time.time() - start_time))
