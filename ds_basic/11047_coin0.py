# 13분
import sys

###################
# 정답 코드
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()
ans = 0
for coin in coins:
    ans += K//coin
    K %= coin
print(ans)
###################

def get_min_coin_num(N, K):
    coins = set()
    for _ in range(N):
        coins.add(int(sys.stdin.readline()))

    min_coin_num = 0

    for c in sorted(coins, reverse=True):
        if K // c > 0:
            min_coin_num += K // c
            K = K % c
        if K == 0:
            return min_coin_num

if __name__ == "__main__":
    N, K = [ int(i) for i in sys.stdin.readline().split(" ")]
    print(get_min_coin_num(N, K))

        
