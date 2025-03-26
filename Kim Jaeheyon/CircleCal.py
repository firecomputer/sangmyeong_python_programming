# Getting radius from input
print("# 원의 반지름을 입력받아 원의 지름과 면적을 계산하는 프로그램입니다.")
radius = float(input("먼저 반지름(radius)을 입력해주세요: "))

# Calculating
print()
print()
print()
print("처리 중입니다...")
diameter = radius * 3.14*2     # diameter of circle = radius * π * 2
area = ( radius ** 2 ) * 3.14  # area of circle = radius * radius * π

# Printing Result
print()
print()
print()
print("결과는 다음과 같습니다:")
print(f"원의 지름: {diameter}")
print(f"원의 면적: {area}")

# Stopping Program
print("프로그램을 종료합니다.")