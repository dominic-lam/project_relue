import time
import concurrent.futures

def iterative_process(n:int, chain:[int]):
    if n == 1:
        return chain

    if n%2 == 0:
        k = int(n/2)
        chain.append(k)
        return iterative_process(k, chain)
    else:
        k = int(3*n+1)
        chain.append(k)
        return iterative_process(k, chain)

def get_next_number(n: int):
    if n%2 == 0:
        return int(n/2)
    else:
        return int(3*n+1)

chain_count_dict = {1:1}
def get_chain_count(n: int):
    if n in chain_count_dict:
        return chain_count_dict[n]

    if n%2 == 0:
        return get_chain_count(int(n/2)) + 1
    else:
        return get_chain_count(int(3*n+1)) + 1


if __name__ == '__main__':
    start_time = time.time()

    # #Method 1, Single Processor
    # # ---Time spent:  25.65583872795105 seconds ---
    # max_chain_count = 0
    # max_int = 0
    # max_chain = []
    # for i in range(1,1000000):
    #     chain = iterative_process(i, [i])
    #     chain_count = len(chain)
    #     if chain_count > max_chain_count:
    #
    #         max_chain_count = chain_count
    #         max_int = i
    #         max_chain = chain
    #
    # print(max_int, chain_count, chain)

    # #Method 2, Multi-Processor
    # # ---Time spent:  272.59565782546997 seconds ---
    # chains = []
    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     ls = list(range(1,1000000))
    #     # print(ls)
    #     chain_list = []
    #     for i in ls:
    #         chain_list.append([i])
    #     # print(chain_list)
    #     chains = executor.map(iterative_process, ls, chain_list)
    #
    # max_int = 0
    # max_chain = []
    # max_chain_count = 0
    # for chain in chains:
    #     chain_count = len(chain)
    #     if chain_count > max_chain_count:
    #         max_chain = chain
    #         max_int = chain[0]
    #         max_chain_count = chain_count
    #
    # print(max_int, max_chain_count, max_chain)
    #
    #


    # #Method 3, Record number and chain count in a dictionary,
    # # adopt the record if we meet the number we did before in the interation process.
    # # it took about 1.86s to find the answer 837799
    # i = 2
    # dict = {1: 1}
    # longest_i = 2
    # longest_chain_count = 1
    # while i < 1000000+1:
    #     count = 1
    #     n = i
    #
    #     #This while loop can be done in a recursive function
    #     while n != 1:
    #         n = get_next_number(n)
    #         if n in dict:
    #             count += dict[n]
    #             n = 1
    #         else:
    #             count += 1
    #             if n == 1:
    #                 break
    #     dict[i] = count
    #
    #     if longest_chain_count < count:
    #         longest_chain_count = count
    #         longest_i = i
    #
    #     i += 1
    # print(longest_i, longest_chain_count)
    #
    # Result
    # # 837799 525
    # # ---Time spent:  1.875133752822876 seconds ---

    #Method 4, modify method 3 with a recursive function
    i = 2
    longest_i = 2
    longest_chain_count = 1
    while i < 1000000+1:
        count = get_chain_count(i)
        chain_count_dict[i] = count
        if longest_chain_count < count:
            longest_chain_count = count
            longest_i = i

        i += 1
    print(longest_i, longest_chain_count)
    # 837799 525
    # ---Time spent:  1.3594722747802734 seconds ---
    #So it spent a little bit lesser time than method3 and the code is much more cleaner


    print("---Time spent:  %s seconds ---" % (time.time() - start_time))