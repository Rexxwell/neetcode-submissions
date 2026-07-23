class Solution:
    # One pass hash maps and hash sets
    # Runtime: 28ms
    # Memory: 8.0 MB
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        r = 0

        while r < 9:
            c = 0
            while c < 9:
                num = board[r][c]
                row = rows[r]
                column = columns[c]
                square = squares[(r // 3, c // 3)]

                if num != ".":
                    # row
                    if num in row:
                        # Duplicate found in rows[r]
                        return False
                    else:
                        row.add(num)

                    # column
                    if num in column:
                        # Duplicate found in columns[c]
                        return False
                    else:
                        column.add(num)
                    
                    # square
                    if num in square:
                        # Duplicate found in squares[(r // 3, c // 3)]
                        return False
                    else:
                        square.add(num)
                
                c += 1

            r += 1
        
        print("Rows:", rows)
        print("Columns:", columns)
        print("Squares:", squares)
        return True