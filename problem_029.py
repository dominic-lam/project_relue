import math
if __name__ == '__main__':
    outcomes = []
    n = 100
    for a in range(2,n+1):
        for b in range(2,n+1):
           outcome = math.pow(a,b)
           if not outcome in outcomes:
               outcomes.append(outcome)
    outcomes = sorted(outcomes)
    print(len(outcomes), outcomes)