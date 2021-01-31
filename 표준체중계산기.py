
#__________________________________________________________________________________________________표준체중 계산기
def std_weight(height , gender):
    if gender == "남자":
        weight = round(float((height/100) * (height/100) * 22),2)
        print("키 {}cm 남자의 표준 체중은 {}kg입니다.".format(int(height), weight))
    else : 
        weight = round(float((height/100) * (height/100) * 21),2)

        print("키 {}cm 여자의 표준 체중은 {}kg입니다.".format(int(height), weight))
height = float(input("키를 입력하세요 :"))
gender = input("성별을 입력하세요 :")
std_weight(height, gender)

