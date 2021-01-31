#__________________________________________________________________________________________________함수
# def open_account(): # 함수정의
#     print("새로운 계좌가 생성되었습니다.")
# open_account()
#__________________________________________________________________________________________________전달값, 반환값
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {} 원 입니다.".format (balance+money))
#     return balance + money # 값 반환
# def withdraw(balance, money):
#     if balance >= money : 
#         print("출금이 완료되었습니다. 잔액은 {} 원입니다".format(balance - money))
#         return balance - money
#     else :
#         print("잔액이 모자랍니다. 잔액은 {}입니다".format(balance))
#         return balance
# def withdraw_nihgt(balance, money):
#     commission = 100 
#     return commission, balance - money - commission
# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
# commission, balance = withdraw_nihgt(balance, 500)
# print("수수료는 {}원입며, 잔액은 {}원입니다.".format(commission, balance))
#__________________________________________________________________________________________________기본값
# def profile(name, age , main_lang):
#     print("이름 : {}\t나이 : {}\t주 사용 언어 : {}"\
#         .format(name, age, main_lang))
# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")
# def profile(name="강백호", age=17 , main_lang="파이썬"):
#     print("이름 : {}\t나이 : {}\t주 사용 언어 : {}"\
#         .format(name, age, main_lang))
# profile("유재석")
# profile("조혜련")
#__________________________________________________________________________________________________키워드값
# def profile(name, age, main_lang):
#     print(name, age, main_lang)
# profile(name="유재석",main_lang="파이썬",age=20)
# profile(main_lang="파이썬",age=20,name="유재석")
#__________________________________________________________________________________________________가변인자
# def profile(name, age, *language):
#     print("이름:{}\t나이:{}\t".format(name,age), end="") # end - 끝날때 자동줄넘김이 아닌 엔드의 내용으로 대체
#     for lang in language:
#         print(lang, end=" ")
#     print()
# profile("유재석",20,"파이선","자바","C","C++","C#","GO")
# profile("김테호",25,"코틀린","스위프트","","","")
#__________________________________________________________________________________________________지역변수, 전역변수
# gun = 10 # 전역변수 gun
# # def checkpoint(soldiers):
# #     # gun = 20 # 지역변수 gun
# #     global gun # 전역공간에 있는  gun 사용
# #     gun = gun - soldiers
# #     print("[함수 내] 남은 총 : {}".format(gun))
# def checkpoint_ret(gun, soldiers):
#         gun = gun - soldiers
#         print("[함수 내] 남은 총 : {}".format(gun))
#         return gun # 출력값을 gun 에 입력
# print("전체 총 : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))
#__________________________________________________________________________________________________퀴즈
# def std_weight(height, gender):
#     if gender == "남자":
#         weight = round(float(height * height * 22),2)
#         height2 = int(height * 100) 
#         print("키 {}cm 남자의 표준 체중은 {}kg입니다.".format(height2, weight))
#     else : 
#         weight = round(float(height * height * 21),2)
#         height2 = int(height * 100) 
#         print("키 {}cm 여자의 표준 체중은 {}kg입니다.".format(height2, weight))
# height = float(input("키를 입력하세요 :"))
# gender = input("성별을 입력하세요 :")
# std_weight(height, gender)

# def std_weight(height,gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21
# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender),2)
# print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height, gender, weight))