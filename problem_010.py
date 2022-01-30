if __name__ == '__main__':
    prime_list = [2]
    sum = 2

    i = 2
    limit = 2000000
    while prime_list[-1] < limit:

        is_prime = True
        for j in prime_list:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
            print(i)
            if i < limit:
                sum += i
            else:
                break
        i += 1
    print(sum)