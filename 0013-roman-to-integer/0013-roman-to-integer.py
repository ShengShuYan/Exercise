class Solution:
    def romanToInt(self, s: str) -> int:
        L = iter(s)
        T = 0
        P = next(L)
        while True:
            H = next(L, None)
            if P == 'I':
                if H == 'V':
                    T += 4
                    P = next(L, None)
                elif H == 'X':
                    T += 9
                    P = next(L, None)
                else: 
                    T += 1
                    P = H
            elif P == 'V':
                T += 5
                P = H
            elif P == 'X':
                if H == 'L':
                    T += 40
                    P = next(L, None)
                elif H == 'C':
                    T += 90
                    P = next(L, None)
                else: 
                    T += 10
                    P = H
            elif P == 'L':
                T += 50
                P = H
            elif P == 'C':
                if H == 'D':
                    T += 400
                    P = next(L, None)
                elif H == 'M':
                    T += 900
                    P = next(L, None)
                else: 
                    T += 100
                    P = H
            elif P == 'D':
                T += 500
                P = H
            elif P == 'M':
                T += 1000
                P = H
            if P is None:
                break
        return T



        