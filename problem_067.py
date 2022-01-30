def setup_triangle():
    f = open('problem_067_triangle.txt', 'r')
    temp_triangle = f.read()
    triangle_rows = temp_triangle.split('\n')
    triangle = []
    for row in triangle_rows:
        r_str = row.split(' ')
        r = []
        for str in r_str:
            r.append(int(str))
        triangle.append(r)
    return triangle

if __name__ == '__main__':
    triangle = setup_triangle()
    for i in range(len(triangle) - 1, 0, -1):
        row = triangle[i-1]
        print(i, row)
        for j in range(0, len(row)):
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])

    print(triangle)