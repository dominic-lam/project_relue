import math, time,decimal

if __name__ == '__main__':
    start_time = time.time()
    #Method 1
    # i = 2
    #
    # while True:
    #     for j in range(1,i):
    #         k = i*i + j*j
    #         if math.sqrt(k).is_integer():
    #             k = math.sqrt(k).__int__()
    #             sum = i+j+k
    #             print(j, i , k, sum)
    #
    #             if sum == 1000:
    #                 print(i*j*k)
    #                 exit()
    #     i+=1

    #Method 2
    #By using Pythagorean Triples Theorem, we may use the formula
    #a = st, b = (s^2 - t^2)/2, c = (s^2 + t^2)/2, s>t>=1 where a is odd
    # therefore s and t must also be odd, b is even
    #to find the required triplet.
    #
    #So, given that a+b+c= 1000.
    #we may conclude that s(s+t) = 1000
    for s in range(3, int(pow(1000,0.5)), 2):
        for t in range(1,s,2):
            if s*(s+t) == 1000:
                # print(s,t)
                a = s*t
                b = (s*s - t*t)/2
                c = (s*s + t*t)/2
                print(int(a*b*c))
                break

    print("---Time spent:  %s ms ---" % ((time.time() - start_time)*1000))

