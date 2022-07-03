def spiralOrder(matrix):
    if not matrix: return []
    ret = []
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    m,n = len(matrix), len(matrix[0])
    x=y=d=0
    
    for i in range(m*n):
        ret.append(matrix[x][y])
        matrix[x][y] = 0
        next_x , next_y = x+dx[d], y+dy[d]
        if next_x >= m or next_x<0 or next_y >= n or next_y<0 or matrix[next_x][next_y]==0:
            d = (d+1)%4
            next_x, next_y = x+dx[d], y+dy[d]
        x,y = next_x, next_y
    return ret


def findDiagonalOrder(matrix):
    
    # Check for an empty matrix
    if not matrix or not matrix[0]:
        return []
    
    # The dimensions of the matrix
    N, M = len(matrix), len(matrix[0])
    
    # Incides that will help us progress through 
    # the matrix, one element at a time.
    row, column = 0, 0
    
    # As explained in the article, this is the variable
    # that helps us keep track of what direction we are
    # processing the current diaonal
    direction = 1
    
    # Final result array that will contain all the elements
    # of the matrix
    result = []
    
    # The uber while loop which will help us iterate over all
    # the elements in the array.
    while row < N and column < M:
        
        # First and foremost, add the current element to 
        # the result matrix. 
        result.append(matrix[row][column])
        
        # Move along in the current diagonal depending upon
        # the current direction.[i, j] -> [i - 1, j + 1] if 
        # going up and [i, j] -> [i + 1][j - 1] if going down.
        new_row = row + (-1 if direction == 1 else 1)
        new_column = column + (1 if direction == 1 else -1)
        
        # Checking if the next element in the diagonal is within the
        # bounds of the matrix or not. If it's not within the bounds,
        # we have to find the next head. 
        if new_row < 0 or new_row == N or new_column < 0 or new_column == M:
            
            # If the current diagonal was going in the upwards
            # direction.
            if direction:
                
                # For an upwards going diagonal having [i, j] as its tail
                # If [i, j + 1] is within bounds, then it becomes
                # the next head. Otherwise, the element directly below
                # i.e. the element [i + 1, j] becomes the next head
                row += (column == M - 1)
                column += (column < M - 1)
            else:
                
                # For a downwards going diagonal having [i, j] as its tail
                # if [i + 1, j] is within bounds, then it becomes
                # the next head. Otherwise, the element directly below
                # i.e. the element [i, j + 1] becomes the next head
                column += (row == N - 1)
                row += (row < N - 1)
                
            # Flip the direction
            direction = 1 - direction        
        else:
            row = new_row
            column = new_column
                    
    return result                 