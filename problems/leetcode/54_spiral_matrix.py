def spiral_matrix(matrix):
    res = []
    if len(matrix) == 0:
        return res
    row = len(matrix)
    col = len(matrix[0])

    top, bottom, left, right = 0, row - 1, 0, col - 1

    while(top <= bottom and left <= right):
        # Top
        for idx in range(left, right + 1):
            res.append(matrix[top][idx])

        top += 1

        # Right
        for idx in range(top, bottom + 1):
            res.append(matrix[idx][right])

        right -= 1
        
        # Bottom
        if top < bottom or row == 2:
            for idx in reversed(range(left, right + 1)):
                res.append(matrix[bottom][idx])

            bottom -= 1

        # Left
        if left < right or col == 2:
            for idx in reversed(range(top, bottom + 1)):
                res.append(matrix[idx][left])

            left += 1
    return res

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4, 5, 6], 
        [7, 8, 9, 10, 11, 12]
    ] 
    print(spiral_matrix(matrix))
