class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        sa = {A[0]}
        sb = {B[0]}
        C = [None] * n
        if A[0] == B[0]:
            C[0] = 1  
        else:
            C[0] = 0
        for i in range(1, n):
            if A[i] not in sa and A[i] in sb:
                C[i] = C[i-1] + 1
            else:
                C[i] = C[i-1]
            sa.add(A[i])
            if B[i] not in sb and B[i] in sa:
                C[i] = C[i] + 1
            sb.add(B[i])

        return C
        