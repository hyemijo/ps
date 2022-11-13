from collections import deque

# def get_final_card(N):
#     dq = deque()
#     for i in range(1, N+1):
#         dq.append(i)

#     while len(dq) != 1:
#         dq.popleft()
#         dq.append(dq.popleft())

#     card = dq.pop()
#     return card


def get_final_card(N):
    dq = deque()
    
    if N % 2: # 홀수
        for i in range(2, N, 4):
            dq.append(i)
    else: # 짝수
        for i in range(4, N+1, 4):
            dq.append(i)
        dq.appendleft(N)
        print(dq)

    
    while len(dq) != 1:
        dq.popleft()
        dq.append(dq.popleft())

    card = dq.pop()
    return card

        

if __name__ == "__main__":
    n = int(input())
    print(get_final_card(n))

