import sys

def get_min_change(N):
    # N원 거스름돈 최소 동전 수로 환산
    # coins = sorted({10, 50, 100, 500}, reverse=True)
    coins = sorted({100, 400, 500}, reverse=True)
    change = {c:0 for c in coins}

    for c in coins:
        change[c] += N // c
        N = N % c

    return change

print(get_min_change(int(sys.stdin.readline())))
