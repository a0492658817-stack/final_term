def INPUT():
    function_type=input()
    amount=int(input())
    code=[]
    for i in range(amount):
        line=input().split()
        code.append(line)
    return function_type,amount,code

def T(code, amount):
    legal = set("ABCDabcd0123456789@#$!_")
    upper = set("ABCD")
    special = set("@#$!_")

    for i in range(amount):
        pw = code[i][0]   # 取出單一密碼
        if not (2 < len(pw) < 6):   # 或 not (3 <= len(pw) <= 5)
            print("F", end="")
            continue

        # 2. 字元合法
        if any(ch not in legal for ch in pw):
            print("F", end="")
            continue

        # 3. 不可重複
        if len(pw) != len(set(pw)):
            print("F", end="")
            continue

        # 4. 至少一個大寫、一個特殊
        if not any(ch in upper for ch in pw):
            print("F", end="")
            continue

        if not any(ch in special for ch in pw):
            print("F", end="")
            continue

        print("T", end="")

def S(code):
    for pair in code:
        secret, guess = pair[0], pair[1]
        A = 0
        s_rest = []
        g_rest = []
        # 先算 X（位置正確）
        for s, g in zip(secret, guess):
            if s == g:
                A += 1
            else:
                s_rest.append(s)
                g_rest.append(g)

        # 再算 Y（字元正確但位置錯）
        B = 0
        for ch in set(s_rest):
            B += min(s_rest.count(ch), g_rest.count(ch))

        print(f"{A}A{B}B")

def main():
    function_type,amount,code=INPUT()
    if(function_type=="T"):
        T(code,amount)
    elif(function_type=="S"):
        S(code)
main()