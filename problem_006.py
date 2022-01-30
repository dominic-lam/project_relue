if __name__ == '__main__':

    #Find the difference between the sum of the squares
    # of the first one hundred natural numbers and the square of the sum.
    #(1+2+...+100)^2 - (1^2 + 2^2 + 3^2 +... + 100^2)
    #
    # #Method 1
    # sum_of_sq_of_first_100_n = 0
    # sum_of_first_100_n = 0
    # for i in range(1,100+1):
    #     sum_of_sq_of_first_100_n += i*i
    #     sum_of_first_100_n += i
    #
    # sq_of_sum_of_first_100_n = sum_of_first_100_n*sum_of_first_100_n
    # diff = sq_of_sum_of_first_100_n - sum_of_sq_of_first_100_n
    # print(diff)
    #

    #Method 2
    #By considering summing up from for i = 1 to k, (i+1)^3 - i^3,
    #one may find the formula of summing up sqares from 1 to k
    limit = 0
    limit = 100
    sum_of_sq = limit*(2*limit+1)*(limit+1)/6
    sum = limit*(limit+1)/2
    sq_of_sum = sum*sum
    diff = sq_of_sum - sum_of_sq
    print(int(diff))

