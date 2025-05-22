class Car:
    color = ""
    speed = 0

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name
    def getSpeed(self):
        return self.speed

myCar1 = Car("아우디", 0)
myCar2 = Car("벤츠", 30)

print(f"{myCar1.getName()}의 현재 속도는 {myCar1.getSpeed()}km입니다.")
print(f"{myCar2.getName()}의 현재 속도는 {myCar2.getSpeed()}km입니다.")