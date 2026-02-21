import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        turns = 0
        cost = 0
        n = len(costs)

        l_l = []
        l_r = []
        index_l = 0
        index_r = n-1
        if len(costs) > 2 * candidates:

            while len(l_l) < candidates:
                l_l.append(costs[index_l])
                index_l += 1
            heapq.heapify(l_l)
            while len(l_r) < candidates:
                l_r.append(costs[index_r])
                index_r -= 1
            heapq.heapify(l_r)

            while turns < k and index_l <= index_r:

                if l_l[0] <= l_r[0]:
                    cost += heapq.heappop(l_l)
                    heapq.heappush(l_l,costs[index_l])
                    index_l += 1
                else:
                    cost += heapq.heappop(l_r)
                    heapq.heappush(l_r, costs[index_r])
                    index_r -= 1

                turns += 1

            heap_combine = l_l + l_r
            
        else:
            heap_combine = costs

        heapq.heapify(heap_combine)
        while turns < k:
            cost += heapq.heappop(heap_combine)           
            turns += 1    

        return cost

        





        