class Car:
    color = ""
    speed = 0
    count = 0

    def __init__(self):
        self.speed = 0
        Car.count += 1

myCar1, myCar2 = None, None

myCar1 = Car()
myCar1.speed = 30

print(f"자동차1의 현재 속도는 {myCar1.speed}km, 생산된 자동차는 총 {Car.count}대입니다.")

myCar1 = Car()
myCar1.speed = 60

print(f"자동차1의 현재 속도는 {myCar2.speed}km, 생산된 자동차는 총 {myCar2.count}대입니다.")