# Mode 입력
mode = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 : "))

# Mode 1
if mode == 1:
    calculation = input("*** 수식을 입력하세요 : ")
    result = eval(calculation) # 이발은 보안 위험이 크기에 Developmental 프로그램엔 적합하지 않음
    print(f"{calculation} 실행 결과는 {result}입니다.")

# Mode 2
elif mode == 2:
    firstNum = int(input("*** 첫번째 숫자를 입력하세요 : "))
    secondNum = int(input("*** 두번째 숫자를 입력하세요 : "))
    result = 0
    for i in range(firstNum, secondNum+1):
        result += i
    print(f"{firstNum}+...+{secondNum}는 {result}입니다.")

# Mode None
else:
    print("잘못된 값을 입력하였습니다")