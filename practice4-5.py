#____________________________________________________________________________________________________________ 문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이선은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고, 
# 파이썬은 쉬워요
# """
# print(sentence3)
#____________________________________________________________________________________________________________ 슬라이싱
# jumin ="990210-1183119"
# print("성별:"+jumin[7])
# print("연:"+jumin[0:2])
# print("월:"+jumin[2:4])
# print("일:"+jumin[4:6])
# print("생년월일:"+jumin[:6]) # 첫자리 는 생략가능
# print("뒤 7자리:" +jumin[7:14]) # 마지막 자리는 생략가능
# print("뒤 7자리부터"+jumin[-7:]) # -는 문자열을 뒤에서부터 카운트함
# ____________________________________________________________________________________________________________ 문자열 처리함수
# python = "Python is Amazingnnnnnnnnnnnn"
# print(python.lower()) # 전체 소문자출력
# print(python.upper()) # 전체 대문자출력
# print(python[0].isupper()) # 대문자인지 진위여부 파악
# print(len(python)) # 문자열 길이 
# print(python.replace("Python", "Java"))  # 문자열에서 특정내용을 변경
# index = python.index("n") # 특정문자 위치 검색 
# print(index)
# index = python.index("n", index + 1 ) # 다음순번 검색
# print(index)
# print(python.find("is")) # 검색기능, 출력값을 참, 거짓
# print(python.count("n")) # 카운트
#____________________________________________________________________________________________________________ 문자열 포맷
#print("a"+"b")
# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아해요." %"파이선")
# print("Apple 은 %c로 시작해요" %"A")
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
# print("나는 {}살입니다.".format(20))
# print("나는 {1}색과 {1}색을 좋아해요". format("파란", "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20,  color = "빨간"))
# age =20 
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")
#____________________________________________________________________________________________________________ 탈출문자
# # \n - 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")
# # \' , \" - 문장내 따옴표 그대로 출력
# print("저는 \"나도코딩\" 입니다.") #저는 "나도코딩" 입니다.
# # \\ : 문장 내에서 \ 출력
# print("C:\\Users\\ggozl\\OneDrive\\바탕 화면\\python work space") #C:\Users\ggozl\OneDrive\바탕 화면\python work space
# # \r : 커서를 맨 앞으로 이동  
# print("Red Apple \rPine") #PineApple
# # \b : 백스페이스( 한글자 삭제)
# print("Redd\bApple") # RedApple
# # \t :탭 
# print("Red\tApple") #Red     Apple
#____________________________________________________________________________________________________________문제
# site = "http://naver.com"
# del_str = site.replace("http://", "")
# print(del_str)
# main_str = del_str[:del_str.index(".")]
# print(main_str)
# password =main_str[0:3]+str(len(main_str))+str(main_str.count("e"))+"!"
# print(f"{site}의 패스워드는 {password}입니다.")
#____________________________________________________________________________________________________________리스트
#순서를 따지는 객체집합  
# subway=[10,20,30] # 배열생성
# print(subway) 
# subway = ["유재석","강호동","박명수"]
# print(subway)
# print(subway.index("강호동")) # 특정 배열 내용물의 위치 출력
# subway.append("하하") # 배열 추가( 맨 뒤로)
# print(subway)
# subway.insert(1, "정형돈") #  특정 순서에 배열추가
# # print(subway)
# # print(subway.pop()) # 뒤에서부터 배열 제거
# # print(subway)
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석")) # 배열내 갯수 세기
# num_list = [5,3,1,4,2]
# num_list.sort()  # 정렬
# print(num_list)  # 
# num_list.reverse() # 역정렬
# print(num_list)  # 
# num_list.clear() # 삭제
# print(num_list)
# mix_list = ["조세호", 20, True]
# print(mix_list)
# num_list.extend(mix_list) # 배열 합병, 피합병이 뒤로 
# print(num_list)
#____________________________________________________________________________________________________________사전
# cabinet = {3:"유재석", 100:"강호동"}
# print(cabinet[3]) # 키가 없을때 에러로 프로그램을 종료시킴
# print(cabinet[100])
# print(cabinet.get(3))  # 키가 없을때 None 값을 출력시키고 코드는 실행시킴
# print(cabinet.get(5, "사용가능")) # 키값에 매칭되는 값이 없을때 정해진 결과값 출력
# print(3 in cabinet) # 존재여부에 대한 진위판별
# cabinet = {"A-3":"유재석", "B-100":"강호동"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호" # 추가, 이미 존재한다면 덮어씌움
# print(cabinet)
# del cabinet["A-3"] # 삭제 
# print(cabinet)
# print(cabinet.keys())  #키값만 출력
# print(cabinet.values()) # 밸류만 출력
# print(cabinet.items()) # 키,밸류 쌍으로 출력
# cabinet.clear() # 삭제
# print(cabinet)
#____________________________________________________________________________________________________________튜플
#변경되지 않는 목록에 활용가능
# menu = ("돈가스","치즈가스")
# print(menu[0])
# print(menu[1])
# name="김종국"
# age = 20 
# hobby = "코딩"
# print(name,age,hobby)
# name, age, hobby = "김종국",20,"코딩"
# print(name,age,hobby)
#____________________________________________________________________________________________________________세트
#집합, 중복안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)
# java={"유재석","김태호","양세형"}
# python=set(["유재석","박명수"])
# #교집합
# print(java & python)
# print(java.intersection(python))
# #합집합
# print(java | python)
# print(java.union(python))
# #차집합
# print(java - python)
# print(java.difference(python))
# python.add("김태호")
# print(python)
# java.remove("김태호")
# print(java)
#____________________________________________________________________________________________________________자료구조의 변경
# menu = {"커피","우유","주스"}
# print(menu, type(menu)) # 해당 배열의 타입 출력
# menu = list(menu)       # 리스트 타입으로 출력
# print(menu, type(menu))
# menu = tuple(menu)      #튜블타입으로 출력
# print(menu, type(menu))
# menu = set(menu)
# print(menu, type(menu))
#____________________________________________________________________________________________________________퀴즈
# from random import *
# users = range(1,21)
# users = list(users)
# shuffle(users)
# winners = sample(users,4)
# print("""--당첨자 발표--
# 치킨 당첨자 : {}
# 커피 당첨자 : {}
# --축하합니다--""".format(winners[0], winners[1:]))
