# 8분 소요
# solution1
# import sys
# from itertools import combinations

# heights = []

# for _ in range(9):
#     heights.append(int(sys.stdin.readline()))

# for c in combinations(heights, 7):
#     if sum(c) == 100:
#         for height in sorted(c):
#             print(height)
#         sys.exit()



# solution 2
# import sys
# from itertools import combinations

# heights = []
# SUM_ALL = 0

# for _ in range(9):
#     heights.append(int(sys.stdin.readline()))
#     SUM_ALL += heights[-1]

# TGT_NUM = SUM_ALL - 100

# for c in combinations(heights, 2):
#     if sum(c) == TGT_NUM:
#         for _c in c:
#             heights.remove(_c)
#         for height in sorted(heights):
#             print(height)
#         sys.exit()


# solution3: w/o combinations
import sys
heights = []

for _ in range(9):
    heights.append(int(sys.stdin.readline()))

TARGET_NUM = sum(heights) - 100
heights = sorted(heights)

for i, h1 in enumerate(heights[:-1]):
    for j, h2 in enumerate(heights[i+1:]):
        if h1 + h2 == TARGET_NUM:
            for k, h in enumerate(heights):
                if k in (i, i+1+j):
                    continue
                print(h)
            sys.exit()


