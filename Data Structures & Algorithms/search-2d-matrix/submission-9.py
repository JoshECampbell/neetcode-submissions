class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) - 1
        k = 0
        while k <= i:
            mid_row = (i + k) // 2
            row = matrix[mid_row]

            if (target >= row[0]) and (target <= row[-1]): 
                j = len(row) - 1
                l = 0
                while l <= j: 
                    mid = (j+l) // 2 
                    if target == row[mid]: 
                        return True 
                    elif target > row[mid]: 
                        l = mid +1 
                    else: 
                        j = mid -1 
                return False
            
            elif target > row[-1]: 
                k = mid_row + 1
            else: 
                i = mid_row - 1
        return False  




                