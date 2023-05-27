class Solution:
    """
    top, bottom, left, right pointers
    while top != bottom and right != left:
        go from left to right:
            add matrix[top][i] to result
        bring top lower
        go from top to bottom:
            add matrix[i][right] to result
        bring right one to the left
        go from right to left:
            add matrix[bottom][i] to result
        bring bottom one up
        go from bottom to top:
            add matrix[i][left] to result
        bring left one right
    
    t 2
    b 1
    l 2
    r 1

    1 2 3 6 9 8 7 4 5

    t 2
    b 2
    l 1
    r 2

    # Solution: O(mn), iterate using pointers
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)
        left = 0
        right = len(matrix[0])
        result = []
        while True:
            for i in range(left,right):
                result.append(matrix[top][i])
            top += 1
            if top == bottom:
                break
            for i in range(top,bottom):
                result.append(matrix[i][right-1])
            right -= 1
            if right == left:
                break
            for i in range(right-1,left-1, -1):
                result.append(matrix[bottom-1][i])
            bottom -= 1
            if top == bottom:
                break
            for i in range(bottom-1, top-1, -1):
                result.append(matrix[i][left])
            left += 1
            if left == right:
                break
        return result
