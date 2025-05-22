class Car:
    color = ""
    speed = 0

    def __init__(self):
        self.color = "빨강"
        self.speed = 0

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

myCar1 = Car()
myCar2 = Car()

print(f"자동차1의 색상은 {myCar1.color}이며, 현재 속도는 {myCar1.speed}km입니다.")
print(f"자동차2의 색상은 {myCar2.color}이며, 현재 속도는 {myCar2.speed}km입니다.")

