def INPUT():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    return N, S

def eval_paren(expr):
    """
    回傳 (result_string, ok)
    ok=False 代表運算格式不合法 => 視為 Hierarchy Violation
    規則：只允許
      - 純字串：abc
      - 字串+字串：a+b
      - 字串*數字 或 數字*字串：ab*3 或 2*YY
    且運算符至多一個
    """
    if expr == "":
        return "", True

    plus_cnt = expr.count('+')
    star_cnt = expr.count('*')

    # 不允許同時出現或出現多次
    if (plus_cnt and star_cnt) or plus_cnt > 1 or star_cnt > 1:
        return "", False

    if plus_cnt == 1:
        a, b = expr.split('+')
        if a == "" or b == "":
            return "", False
        return a + b, True

    if star_cnt == 1:
        a, b = expr.split('*')
        if a == "" or b == "":
            return "", False
        if a.isdigit():
            return b * int(a), True
        if b.isdigit():
            return a * int(b), True
        return "", False

    # 沒有運算符：原樣
    return expr, True

def solve_one(s):
    level = {'{': 3, '[': 2, '(': 1}
    openers = "{[("
    closers = ")]}"
    match = {')': '(', ']': '[', '}': '{'}
    # stack 每個元素： (括號字元, buffer_list)
    stack = [('#', [])]   # root
    unbalanced = False
    violation = False

    for ch in s:
        if ch in openers:
            # 層級檢查：內層不能出現更高層級
            top_br = stack[-1][0]
            if top_br in level and level[ch] > level[top_br]:
                violation = True
            stack.append((ch, []))

        elif ch in closers:
            if len(stack) == 1:
                unbalanced = True
                continue

            open_br, buf = stack.pop()
            if match[ch] != open_br:
                unbalanced = True
                continue

            inner = "".join(buf)
            if open_br == '(':
                inner, ok = eval_paren(inner)
                if not ok:
                    violation = True

            # 把結果塞回上一層
            stack[-1][1].append(inner)

        else:
            # + * 只有在小括號()內才當作運算符；其他地方視為「不運算的連接符」直接忽略
            if ch in "+*" and stack[-1][0] != '(':
                continue
            stack[-1][1].append(ch)

    if len(stack) != 1:
        unbalanced = True

    result = "".join(stack[0][1])
    return unbalanced, violation, result

def main():
    N, S = INPUT()
    for s in S:
        unbalanced, violation, result = solve_one(s)
        if unbalanced:
            print("Unbalanced")
        elif violation:
            print("Hierarchy Violation")
        else:
            print(result)

main()
