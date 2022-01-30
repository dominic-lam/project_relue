import concurrent.futures
import utilities

if __name__ == '__main__':

    prime_list = list(i for i in range(2,20) if utilities.is_prime(i))

    factors_of_target = prime_list
    #First get the prime numbers list from 1 to 20

    for x in range(2,20):
        z = x
        for y in factors_of_target:
            if z % y == 0 & (z / y).__int__() != 1:
                z = (z / y).__int__()
        if z != 1:
            print(x, factors_of_target, z)
            factors_of_target.append(z)
            factors_of_target.sort()

    target = 1
    for f in factors_of_target:
        target *= f
    print(target, factors_of_target)