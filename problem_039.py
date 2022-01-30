import math

def find_solutions(p):
    solutions = []
    for i in range(1, p):
        b = (p*(p-2*i))/(2*(p-i))
        if b.is_integer() and b > 0:
            c = math.sqrt(i*i + b*b)
            if c.is_integer():
                solutions.append([p, i, b, c])
                print(p, i, b, c)
    if len(solutions) > 0:
        return solutions
    return None

if __name__ == '__main__':
    max_solutions_count = 0
    solutions = []
    results = []
    for i in range(1, 1000):
        solution = find_solutions(i)
        if solution != None:
            results.append((solution[0][0], len(solution) / 2))
            if len(solution) > max_solutions_count:
                max_solutions_count = len(solution)
                solutions = solution


    print(max_solutions_count, solutions)
    print(solutions[0][0], 'has', max_solutions_count/2, 'different sets of solution')
