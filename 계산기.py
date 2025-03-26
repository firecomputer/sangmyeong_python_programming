print('수식을 계산하려면 1, 두 수 사이의 합계를 구하려면 2를 누르세요')

x = int(input('입력>'))



if x == 1:
    print('***수식을 입력하세요')
    a = input('입력>')
    a = eval(a)
    print('계산 결과는' + str(a)+'입니다!')

if  x == 2:
    print('첫 번째 숫자를 입력하세요')
    b = int(input('입력>'))
    print('두 번째 숫자를 입력하세요')
    c = int(input('입력>'))
    d = (c**2-b**2+b+c)/2
    print('계산결과는'+ str(d) + '입니다!')



