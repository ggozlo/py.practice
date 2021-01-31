#___________________________________________________________________________________________________ 멤버변수
class Unit:
    def __init__(self, name, hp): 
        self.name =name
        self.hp = hp 
wraith1 = Unit("레이스",80)
print("유닛이름 : {}, 체력 : {}".format(wraith1.name,wraith1.hp))

wraith1.clocking = True # 레이스에 클록킹 변수를 추가
if wraith1.clocking == True:
    print("{} 는 현재 클로킹 상태입니다.".format(wraith1.name))