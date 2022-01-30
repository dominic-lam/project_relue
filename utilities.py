import math, primesieve
import itertools

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

def check_if_palindromic(n:int):
    a = str(n)
    b = a[::-1]
    return a==b


def check_if_1_to_9_pandigital(string):
    list = sorted(string)

    if '0' in list:
        return False

    if not checkIfDuplicates_1(list) and len(list) == 9:
        return True

def check_if_0_to_9_pandigital(string):
    list = sorted(string)

    if not checkIfDuplicates_1(list) and len(list) == 10:
        return True


def check_if_1_to_7_pandigital(string):
    list = sorted(string)

    if '0' in list or '8' in list or '9' in list:
        return False

    if not checkIfDuplicates_1(list) and len(list) == 7:
        return True

def check_if_1_to_8_pandigital(string):
    list = sorted(string)

    if '0' in list or '8' in list:
        return False

    if not checkIfDuplicates_1(list) and len(list) == 8:
        return True

def get_digital_sum(n:int):
    return sum(int(l) for l in str(n))

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

def sigma(k:int, prime_list:[int]):
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

    return int(sigma)


def get_prime_list_under_n(n):
    prime_list = [2,3]

    i = 5
    while i < n:

        if i%3 ==0:
            i += 2
            continue
        i_is_prime = True

        for p in prime_list:
            if p > i**0.5:
                break

            if i%p == 0:
                i_is_prime = False
                break
        if i_is_prime:
            prime_list.append(i)

        # print(i, prime_list)
        i+=2

    return prime_list

def get_prime_list_under_n_with_primesieve(n):
    return primesieve.primes(n)


def is_prime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    if n==3:
        return True

    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)

    if sum % 3 == 0:
        return False

    for i in range(5, math.sqrt(n).__int__() + 1, 2): #We can skip all even numbers
        if n % i == 0:
            return False

    return True

def is_triangle_number(k):
    # Note that the general form for Triangle Number T(n) = 1/2*n(n+1) for a positive integer n,
    # Lets suppose a Triangle integer
    #             k = 1/2n(n+1) [2k=n(n+1) (*)]
    #             k > n^2/2

    #       sqrt(k) > n/sqrt(2)
    #             n < sqrt(2k)
    # Therefore, we may check if n(n+1) = 2k (where n is largest integer < sqrt(2k) (**)), if so we
    # may conclude that k is a Triangle Integer.
    #
    # ** lim sqrt(2k) - n = lim sqrt(n(n+1)) - n = 1/2, therefore the sqrt(2k) = n + d where d is
    # from sqrt(2) - 1 = (0.4142) to 1/2 as n goes from 1 to infinity, so we can conclude that the
    # largest integer < sqrt(2k) is the required n in the general form T(n).
    n = round(math.sqrt(2*k)) #By *
    if n*(n+1) == 2*k:
        print(k, 'is the '+str(n)+'-th Triangle Number')
        return True

    return False

def generate_nth_pentagonal_number(n):
    return n*(3*n-1)/2

def is_pentagonal(k):
    n = (1+math.sqrt(1+24*k))/6
    if generate_nth_pentagonal_number(n) == int(k) and n.is_integer():
        return True
    return False

def generate_nth_hexagonal_number(n):
    return n*(2*n-1)

def is_hexagonal(k):
    n = (1+math.sqrt(1+8*k))/4
    if generate_nth_hexagonal_number(n) and n.is_integer():
        return True
    return False



def get_permuations_of_list(l):
    return list(itertools.permutations(l))

def get_the_n_th_triangle_number(n):
    return (1/2)*n*(n+1)

def get_alphabet_value(s: str):
    if s.isupper():
        return ord(s) - 64
    else:
        return ord(s) - 96

def get_problem_number(filename: str):
    #filename should be in format "problem_XXX.py"
    #now we want to return XXX
    number = (filename.split('.'))[0]
    number = (number.split('_'))[1]
    return number

def read_data_from_file(filename: str):
    f = open(filename, 'r')
    return f.read()


def generate_prime_fatorization(n: int):
    # Sum of all divisors
    # First we find all the prime factorization of n
    prime_factor_and_power_list = []
    prime_list = [2, 3]

    if n % 2 == 0:
        power_of_2 = 1
        while True:
            if (n % (2 ** (power_of_2 + 1)) != 0):
                break
            else:
                power_of_2 += 1
        prime_factor_and_power_list.append((2, power_of_2))

    for i in range(3, n + 1, 2):
        # we may start from 3 and skip or even numbers
        i_is_prime = False

        if i in prime_list:
            i_is_prime = True
        else:
            if is_prime(i):
                i_is_prime = True
                prime_list.append(i)

        if i_is_prime and n % i == 0:
            power_of_i = 1
            while True:
                if (n % (i ** (power_of_i + 1)) != 0):
                    break
                else:
                    power_of_i += 1
            prime_factor_and_power_list.append((i, power_of_i))

        product = 1
        for (p, e) in prime_factor_and_power_list:
            product *= pow(p, e)
        if product == n:
            # print(product, prime_factor_and_power_list)
            break

    return prime_factor_and_power_list

def get_prime_fators(x):
    y = int(x / 2)

    prime_list = [2]
    prime_factor_list = []

    if x % 2 == 0:
        prime_factor_list.append(2)
        while x % 2 == 0:
            x = x / 2

    for i in range(3, y + 1, 2):

        # Check if i is a prime number first
        # if i is a prime number, then put it into the prime list
        is_prime = True
        for j in prime_list:
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            prime_list.append(i)

            if x % i == 0:
                prime_factor_list.append(i)
                while x % i == 0:
                    x = x / i

            if x == 1:
                break

    return prime_factor_list


def phi(n):
    if is_prime(n):
        return n-1

    prime_factor_list = generate_prime_fatorization(n)
    phi = 1

    for (p, k) in prime_factor_list:
        phi *= (p ** k - p ** (k - 1))

    return phi

def get_n_th_triangle(n):
    return int(n*(n+1)/2)

def get_n_th_square(n):
    return n*(n)

def get_n_th_pentagonal(n):
    return int(n*(3*n-1)/2)

def get_n_th_hexagonal(n):
    return n*(2*n-1)

def get_n_th_heptagonal(n):
    return int(n*(5*n-3)/2)

def get_n_th_octagonal(n):
    return n*(3*n-2)

def get_n_th_polygonal(n, p):
    if p == 3:
        return get_n_th_triangle(n)
    elif p == 4:
        return get_n_th_square(n)
    elif p == 5:
        return get_n_th_pentagonal(n)
    elif p == 6:
        return get_n_th_hexagonal(n)
    elif p == 7:
        return get_n_th_heptagonal(n)
    elif p == 8:
        return get_n_th_octagonal(n)
    else:
        return 0



if __name__ == '__main__':
    print('Hello')