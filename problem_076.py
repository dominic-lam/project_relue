coin_list = []

def count_ways_to_make_amount(amount:int, max_coin:int):
    ways = 0
    path=[]
    amount = round(amount,2)
    if  amount == 0:
        # print('path ends here')
        return 1, ['end']

    for i in range(len(coin_list)):
        coin_value = coin_list[i]
        if coin_value > max_coin or coin_value > amount:
            continue
        if amount >= coin_value:
            # print('amount:', amount, 'coin_value: ', coin_value)
            (a, b) = count_ways_to_make_amount(amount - coin_value, coin_value)
            ways += a
            path.append(coin_value)
            # print(b)
            path.append(b)

    return ways, path

if __name__ == '__main__':
    # print(count_ways_to_make_amount(0.05, 2))
    coin_list = [x for x in range(1,101)]
    limit = 100
    ways, path = count_ways_to_make_amount(limit,limit-1)
    print(ways)
    # for i in range(len(coin_list) - 1, -1, -1):
    #     coin_amount = coin_list[i]
    #     print(type(coin_amount), coin_amount)