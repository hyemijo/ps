# input: N, M
# N개의 수 중 M개를 합했을 때 그 값이 가장 큰 경우는?
# MAX SUM = 최댓값 2개의 합

import sys
import heapq as hq


def get_max_sum(INPUT_N, SUM_NUM):
    maxs = []

    for _ in range(INPUT_N):
        x = int(sys.stdin.readline())
        
        if len(maxs) < SUM_NUM:
            hq.heappush(maxs, x)

        if maxs[0] < x:# min-heap
            hq.heappushpop(maxs, x)
    
    MAX_SUM = sum(maxs)
    return MAX_SUM


INPUT_N, SUM_NUM = sys.argv[1:3]
print(get_max_sum(int(INPUT_N), int(SUM_NUM)))

        
    


