import math
def is_prime(n):
    if n < 1:
        return False

    for i in range(1, math.sqrt(n).__int__() + 1):
        if n%i == 0 and i!=1:
            return False
    return True

def get_rotations(n):
    rotations = []
    s = str(n)
    for i in range(0, len(s)):
        r = ''
        for j in range(0, len(s)):
            r += s[j-i]
        rotations.append(int(r))

    return rotations

def is_circular_prime(n):
    rotations = get_rotations(n)
    for r in rotations:
        if not is_prime(r):
            return False
    print(n, 'is circular prime')
    return True

if __name__ == '__main__':
    count = 0
    for i in range(2,1000000):
        if is_circular_prime(i):
            count +=1
    print(count)