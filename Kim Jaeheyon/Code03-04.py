# 진법을 입력받는 부분
position_str = input("입력 진수 결정(16/10/8/2) : ")        # 진법을 입력받음
position = int(position_str)                               # Integer로 바꿈 (예외처리는 안배웠으니 포기)

# 값을 입력받는 부분
num_str = input("값 입력 : ")                              # 값을 입력받음
num = int(num_str, position)                              # 진법 변환 함수는 integer를 입력으로 받기에 str에서 변경

# 계산하는 부분
hex_num = hex(num)                                        # 16진수
dec_num = num                                             # 10진수
oct_num = oct(num)                                        # 8진수
bin_num = bin(num)                                        # 2진수

# 출력하는 부분
print(f'16진수 ==> {hex_num}')
print(f'10진수 ==> {dec_num}')
print(f'8진수 ==> {oct_num}')
print(f'2진수 ==> {bin_num}')

# 프로그램 종료