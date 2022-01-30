import math
if __name__ == '__main__':
    s = ''
    for i in range(1,200000):
        s += str(i)
    print(len(s))
    product = 1
    ls = []
    for i in range(0,7):
        index = int(math.pow(10,i))
        k = int(s[index-1])
        ls.append(k)
        print('d('+str(index)+'):', k)
    for r in ls:
        product *= r
    print(product)
