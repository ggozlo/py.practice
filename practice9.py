#___________________________________________________________________________________________________클래스
# __init__ - 생성자
# name = "마린"
# hp = 40
# damage = 5
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {}, 공격력 {}\n".format(hp, damage))
# tank_name = "탱크"
# tank_hp = 150 
# tank_damage = 35
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {}, 공격력 {}\n".format(tank_hp, tank_damage))
# tank_name2 = "탱크"
# tank_hp2 = 150 
# tank_damage2 = 35
# print("{} 유닛이 생성되었습니다.".format(tank_name2))
# print("체력 {}, 공격력 {}\n".format(tank_hp2, tank_damage2))
# def attack(name, location, damage):
#     print("{} : {} 방향으로 적군을 공격 합니다. [공격력 {}]".format(name, location, damage))
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank_name, "1시", tank_damage2)
# class unit:
#     def __init__(self, name, hp, damage):
#         self.name =name
#         self.hp = hp 
#         self.damage = damage
#         print("{}유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {}, 공격력 {}".format(self.hp, self.damage))
# marine1 = unit("마린", 40,5)
# marine2 = unit("마린", 40,5)
# tank =unit("탱크",150,35)
#___________________________________________________________________________________________________ 멤버변수
# class Unit:
#     def __init__(self, name, hp): 
#         self.name =name
#         self.hp = hp 
# wraith1 = unit("레이스",80,5)
# print("유닛이름 : {}, 공격력 : {}".format(wraith1.name,wraith1.damage))
# wraith2 = unit("제어한 레이스", 80 ,5)
# wraith2.clocking = True # 레이스 2에 클록킹 변수를 추가
# if wraith2.clocking == True:
#     print("{} 는 현재 클로킹 상태입니다.".format(wraith2.name))
#___________________________________________________________________________________________________ Method
# class Attackunit:
#     def __init__(self, name, hp, damage):
#         self.name =name
#         self.hp = hp 
#         self.damage = damage
#     def attack(self, location):
#         print("{} | {} 방향으로 적군을 공격 합니다. [공격력 {}]".format(self.name, location, self.damage))
#     def damaged(self, damage):
#         print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {} 입니다. ".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{} : 파괴되었습니다.".format(self.name))
# firebat1 = Attackunit("파이어뱃", 50 ,16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)
#___________________________________________________________________________________________________ 상속
# class Unit:
#     def __init__(self, name, hp): 
#         self.name =name
#         self.hp = hp 
# class Attackunit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#     def attack(self, location):
#         print("{} | {} 방향으로 적군을 공격 합니다. [공격력 {}]".format(self.name, location, self.damage))
#     def damaged(self, damage):
#         print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {} 입니다. ".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{} : 파괴되었습니다.".format(self.name))
# firebat1 = Attackunit("파이어뱃", 50 ,16)
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)
#___________________________________________________________________________________________________ 다중상속class Unit:
# class Unit:   
#     def __init__(self, name, hp):  #부모 클래스
#         self.name =name
#         self.hp = hp 
# class Attackunit(Unit):  # 자식 클래스
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#     def attack(self, location):
#         print("{} | {} 방향으로 적군을 공격 합니다. [공격력 {}]".format(self.name, location, self.damage))
#     def damaged(self, damage):
#         print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {} 입니다. ".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{} : 파괴되었습니다.".format(self.name))
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#     def fly(self, name, location):
#         print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))
# class Flyableattackunit(Attackunit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         Attackunit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)
# valkyrie = Flyableattackunit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name,"3시")
#___________________________________________________________________________________________________ 연산자 오버라이딩class Unit:   
class Unit:
    def __init__(self, name, speed,hp):  #부모 클래스
        self.name =name
        self.hp = hp 
        self.speed = speed
    def move(self,location):
        print("지상 유닛 이동")
        print("{}:{} 방향으로 이동합니다 [속도{}]".format(self.name,location,self.speed))
class Attackunit(Unit):  # 자식 클래스
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, speed, hp)
        self.damage = damage
    def attack(self, location):
        print("{} | {} 방향으로 적군을 공격 합니다. [공격력 {}]".format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다. ".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))
class Flyableattackunit(Attackunit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        Attackunit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    def move(self, location):
        print("공중유닛이동")
        self.fly(self.name, location)
vulture = Attackunit("벌쳐", 80,10, 20)
battlecruiser = Flyableattackunit("배틀크루저",500,25,3)
vulture.move("11시")
#battlecruiser.fly(battlecruiser.name, "11시")
battlecruiser.move( "11시")