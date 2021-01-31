#___________________________________________________________________________________________________클래스
#__init__ - 생성자
name = "마린"
hp = 40
damage = 5
print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {}, 공격력 {}\n".format(hp, damage))

tank_name = "탱크"
tank_hp = 150 
tank_damage = 35
print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {}, 공격력 {}\n".format(tank_hp, tank_damage))

tank_name2 = "탱크"
tank_hp2 = 150 
tank_damage2 = 35
print("{} 유닛이 생성되었습니다.".format(tank_name2))
print("체력 {}, 공격력 {}\n".format(tank_hp2, tank_damage2))

def attack(name, location, damage):
    print("{} : {} 방향으로 적군을 공격 합니다. [공격력 {}]".format(name, location, damage))
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank_name, "1시", tank_damage2)

class unit:
    def __init__(self, name, hp, damage):
        self.name =name
        self.hp = hp 
        self.damage = damage
        print("{}유닛이 생성 되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))
marine1 = unit("마린", 40,5)
marine2 = unit("마린", 40,5)
tank =unit("탱크",150,35)