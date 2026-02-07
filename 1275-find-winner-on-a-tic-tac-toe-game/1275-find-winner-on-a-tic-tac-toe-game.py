class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        count = 0
        A = []
        B = []
        success = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4 ,7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
        for c in moves:
            count += 1
            number = c[0] * 3 + c[1] + 1
            if count % 2 == 1:
                A.append(number)
                AS = set(A)
                if any(c <= AS for c in success):
                    return 'A'
                if count == 9:
                    return 'Draw'
            else:
                B.append(number)
                BS = set(B)
                if any(c <= BS for c in success):
                    return 'B'
        return 'Pending'
        
        