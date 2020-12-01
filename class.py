#클래스

#객체지향 프로그램 (Object Oriented Programming): 
#Self, 클래스, 인스턴스 변수

#선언
# class 클래스명:
#     함수
#     함수
#     함수

#예제1
class UserInfo:
    def __init__(self, name):
        self.name = name
    def user_info_p(self):
        print("name:", self.name)

#네임스페이스      
user1 = UserInfo("Kim")
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))
print(user1.__dict__)

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용가능, 객체보다 먼저 생성

# 예제 2
# self의 이해
class SelfTest():
    # def function1(): #클래스 메서드
    #     print("function1 called")

    def function2(self): #인스턴스 메서드
        print("function2 called")

self_test = SelfTest()
# SelfTest.function1()
self_test.function2()


#예제3
#클래스 변수, 인스턴스 변수


class WareHouse:
    #클래스변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self): #인스턴스가 종료될때? 지웠을떄? 
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee') 

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1 #메모리에서 삭제 

print(user2.stock_num)
print(user3.stock_num)
