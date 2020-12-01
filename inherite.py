#상속, 다중상속

#예제1
#상속 기본
#슈퍼클래스의(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

#라면 -> 속성(종류, 회사, 맛, 종류, 이름) : 부모

class Car:
    def __init__(self, tp, color):
        """parentsClass"""
        self.type = tp
        self.color = color
    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """SubClass"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your car Name : %s " % self.car_name

class BezCar(Car):
    """SubClass"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your car Name : %s " % self.car_name

    def show(self):
        return 'Car Info : %s %s %s' %(self.car_name, self.type, self.color)

#일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Child
print(model1.show()) # Super
print(model1.show_model()) #child
print(model1.__dict__)

# Method Overriding(오버라이딩)
model2 = BezCar("220d", "suv", "black")
print(model2.show())

#Parent Method call
model3 = BezCar("350s","sedan","silver")
print(model3.show())