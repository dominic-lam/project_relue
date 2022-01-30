import math
def is_prime(n):

    if n < 1:
        return False

    for i in range(1, math.sqrt(n).__int__() + 1):
        if n%i == 0 and i!=1:
            return False
    return True

def f_n(a,b,n):
    return n*n+a*n+b

if __name__ == '__main__':
    max_k = 0
    max_k_a = 0
    max_k_b = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            if is_prime(f_n(a,b,0)):
                print('a=', a, ', b=', b, ', n=', 0, ', f_n=', f_n(a, b, 0))
                n = 1

                while True:
                    if is_prime(f_n(a,b,n)):
                        print('a=', a, ', b=', b, ', n=', n, ', f_n=', f_n(a, b, n))
                        n+=1
                    else:
                        print('a=', a, ', b=', b, ', n=', 0, ', f_n=', f_n(a, b, n) , 'is not a prime')
                        k = n-1
                        if k > max_k:
                            max_k = k
                            max_k_a = a
                            max_k_b = b
                            print('max_k registered:', k,'with a, b=', a,b)
                        break

    print(max_k, max_k_a, max_k_b)
    # Result: 70 -61 971