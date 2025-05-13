#진수 입력부분
print('진수를 입력하세요 (16/10/8/2)')
a = int(input('입력>'))

#숫자 입력부분
print('숫자를 입력하세요')
b = int(input('입력>'), a)
        
print(hex(b))
print(b)
print(oct(b))
print(bin(b))

