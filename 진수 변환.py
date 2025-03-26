#진수를 정하는 부분
print('입력 진수를 정하세요(16/10/8/2)')
x = int(input('입력>'))

#값을 정하는 부분
print('값을 입력하세요')
y = int(input('입력>'), x)

a = hex(y)
b = y
c = oct(y)
d = bin(y)

print('16진수의 값은'+ str(a)+ '입니다!')
print('10진수의 값은'+ str(b)+ '입니다!')
print('8진수의 값은'+ str(c)+ '입니다!')
print('2진수의 값은'+ str(d)+ '입니다!')