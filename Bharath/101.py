

def generate_pascals_triangle(rows):
    triangle = []

    for i in range(rows):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                # Each element (except the first and last) is the sum of the two elements above it in the previous row.
                element = triangle[i - 1][j - 1] + triangle[i - 1][j]
                row.append(element)
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(str(num) for num in row).center(len(triangle[-1]) * 3))

if __name__ == "__main__":
    num_rows = 5  # You can change this to generate more rows of Pascal's Triangle
    triangle = generate_pascals_triangle(num_rows)
    print("Pascal's Triangle:")
    print_pascals_triangle(triangle)

    output::   Pascal's Triangle:
       1
      1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1

