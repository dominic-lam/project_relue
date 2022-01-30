import utilities


if __name__ == '__main__':
    list = []
    for i in range(101,1000):
        for j in range(100,i):
            if utilities.check_if_palindromic(i*j):
                print(i,j, i*j)
                list.append(i*j)
    list.sort()
    print('Largest palindromic product:', list[-1])