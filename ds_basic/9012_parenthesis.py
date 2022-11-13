def check_vps(string):
    stack = []
    
    # vps 체크: 문자열 길이 짝수여야 함
    if len(string) % 2:
        print("NO")
        return

    for char in string:
        if stack and stack[-1] == "(" and char == ")":
            stack.pop()
            continue
        stack.append(char)
        
    if stack:
        print("NO")
    else: 
        print("YES")
    return



if __name__ == "__main__":
    num = int(input())
    for i in range(num):
        string = input()
        check_vps(string)
        
        
