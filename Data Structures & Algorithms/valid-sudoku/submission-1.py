class Solution:
    # Manually check each condition
    # Solution with no ai
    # Runtime: 44ms
    # Memory: 8.0 MB
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row is valid.
        for row in board:
            numbers = []

            for num in row:
                if num != ".":
                    if num in numbers:
                        # Duplicate found in the row.
                        return False
                    else:
                        numbers.append(num)
        
        # Check each row column is valid.
        i = 0

        while i < 9:
            numbers = []
            for row in board:
                num = row[i]

                if num != '.':
                    if num in numbers:
                        # Duplicate found in the column.
                        return False
                    else:
                        numbers.append(num)
                
            i += 1

        # Check each 3x3 box is valid.
        i = 0
        j = 2

        while j < 8:
            l = 0
            m = 2

            while m < 8:
                numbers = []

                for r in range(i, j + 1):
                    for s in range(l, m + 1):
                        num = board[r][s]

                        if num != ".":
                            if num in numbers:
                                # Duplicate found in the 3x3.
                                return False
                            else:
                                numbers.append(num)
                
                l += 3
                m += 3

            i += 3
            j += 3
        
        # No duplicates are found anywhere.
        return True
                        