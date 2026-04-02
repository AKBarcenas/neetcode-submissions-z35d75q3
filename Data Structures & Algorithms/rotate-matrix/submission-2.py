class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix[0]) - 1

        while left < right:
            for index in range(right - left):
                top = left
                bottom = right

                topLeft = matrix[top][left + index]

                matrix[top][left + index] = matrix[bottom - index][left]

                matrix[bottom - index][left] = matrix[bottom][right - index]

                matrix[bottom][right - index] = matrix[top + index][right]

                matrix[top + index][right] = topLeft

            left += 1
            right -= 1