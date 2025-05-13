def calc(v1, v2, op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2
    return result

res = calc(float(input("첫번째 수를 입력하세요: ")), float(input("두번째 수를 입력하세요: ")), input("계산 방식을 입력하세요 (+, -, *, /): "))
print(res)