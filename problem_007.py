if __name__ == '__main__':
    prime_list = [2]

    i = 3
    while len(prime_list) < 10001:
        is_prime = True
        for j in prime_list:
            if i % j == 0 and j != 1:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
            print(len(prime_list), i)
        i += 2

    print(prime_list[-1])