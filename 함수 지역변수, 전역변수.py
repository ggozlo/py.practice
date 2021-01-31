#__________________________________________________________________________________________________지역변수, 전역변수
gun = 10 # 전역변수 gun
def checkpoint(soldiers):
    #gun = 20 # 지역변수 gun
    global gun # 전역공간에 있는  gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))
checkpoint(5)

gun = 10
def checkpoint_ret(gun, soldiers):
        gun = gun - soldiers
        print("[함수 내] 남은 총 : {}".format(gun))
        return gun # 출력값을 gun 에 입력
print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))