import time, utilities, os

def check_palindromic_in_both_base(n):
    s = str(n)
    reversed_s = s[::-1]
    reversed_n = int(reversed_s)

    b = bin(n)
    n_b = int((b.split('b'))[1])
    reversed_n_b = int(((b.split('b'))[1])[::-1])

    if n==reversed_n and n_b==reversed_n_b:
        print(n, 'is palindromic in both base, ',n,n_b)
        return True

if __name__ == '__main__':
    problem_number_str = utilities.get_problem_number(os.path.basename(__file__))

    print('Start working on Project Euler Problem: ' + problem_number_str)
    start_time = time.time()

    sum = 0

    for i in range(1, 1000000):
        if check_palindromic_in_both_base(i):
            sum += i
    print(sum)

    print("---Time spent:  %s seconds ---" % (time.time() - start_time))