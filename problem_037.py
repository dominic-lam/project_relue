import math
def is_prime(n):
    if n <= 1:
        return False

    for i in range(1, math.sqrt(n).__int__() + 1):
        if n%i == 0 and i!=1:
            return False
    return True

def check_if_truncatable_prime(n):
    rotations = []
    s = str(n)
    for i in range(len(s)):
        rotations.append(int(s[i:]))

    for i in range(len(s)):
        rotations.append(int(s[:len(s)-i]))

    for r in rotations:
        if not is_prime(r):
            return False

    print(rotations)

    return True

if __name__ == '__main__':
    sum = 0
    truncatable_primes = []
    i = 10
    while len(truncatable_primes) < 11:

        if check_if_truncatable_prime(i):
            truncatable_primes.append(i)
            sum += i
        i+=1


    print(sum)
