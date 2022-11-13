import sys

##########
# 정답 코드
N, L = map(int, input().split())
coord = [False] * 1001
for i in map(int, input().split()):
    coord[i] = True

x = 0
ans = 0
while x < 1001:
    if coord[x]:
        ans += 1
        x += L
    else:
        x += 1
print(ans)

##########



def get_min_tape_num(L):
    leak_points = set()
    for _ in sys.stdin.readline().strip().split(" "):
        leak_points.add(int(_))
    leak_points = sorted(leak_points)

    min_tape_num = 1
    rightmost_taped_point = leak_points[0] + L - 1

    # leak point 왼 -> 오 돌면서 확인
    for p in leak_points[1:]:
        if p > rightmost_taped_point:
            min_tape_num += 1
            rightmost_taped_point = p + L - 1
        
    return min_tape_num

if __name__ == "__main__":
    N, L = map(int, sys.stdin.readline().split(" "))
    print(get_min_tape_num(L))
    

    
