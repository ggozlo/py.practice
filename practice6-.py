#______________________________________________________________________________________________________________________________________if
# weather = input("오늘 날씨는 어때요? ") # 유저 입력
# # if 조건: 
# #     실행 명령문
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지": # elif = else if
#     print("마스크를 챙기세요")
# else:
# #     print("오늘은 날씨가 좋아요")
# temp = float(input("기온은 어떄요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30: 
#     print("괜찮은 날씨에요")
# elif 0<= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")
#______________________________________________________________________________________________________________________________________for
# for waiting_no in range(1, 6):
#     print("대기번호 : {}".format(waiting_no))
# sb = ["아이언맨", "토르", "그루트"] # 배열생성
# for cs in sb:  # sb 배열을 하나씩 cs 에 넣으면서 반복실행
#     print("{}, 커피가 준비되었습니다.".format(cs))
#______________________________________________________________________________________________________________________________________while
# cs = "토르"
# index =5
# while index >= 1:
#     print("{}, 커피가 준비 되었습니다. {}번 남았어요.".format(cs,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분 되었습니다.")
# cs = "아이언맨"
# index = 1
# while True: 
#     print("{}, 커피가 준비 되었습니다.호출{}회".format(cs,index))
#     index +=1
# cs = "토르"
# person = "Unknown"
# while person != cs:
#     print("{}, 커피가 준비 되었습니다.".format(cs))
#     person = input("이름이 어떻게 되세요? ")
#______________________________________________________________________________________________________________________________________continue, break
# absent = [2,5]
# no_book = [7]
# for student in range(1,11):
#     if student in absent:  # absent 와 student 가 일치할때 
#         continue # 조건 충족시 스킵함
#     elif student in no_book:
#         print("오늘수업 여기까지. {}는 교무실로".format(student))
#         break
#     print("{}, 책을 읽어봐".format(student))
#______________________________________________________________________________________________________________________________________한줄 for
# student = [1,2,3,4,5]
# print(student)
# student = [i+100 for i in student] # i에다가 student 배열의 값을 하나씩 불러와서 +100 을 반복
# print(student)
# student = ["아이언맨", "토르", "그루트"]
# print(student)
# student = [len(i) for i in student]
# print(student)
# student = ["iron man", "thor", "groot"]
# print(student)
# student = [i.upper() for i in student]
# print(student)
#______________________________________________________________________________________________________________________________________퀴즈 
# from random import *
# cnt = 0 
# for i in range(1,51): # 1~ 50 수 생성(승객)
#     time = randrange(5,51) # 5~50 소요 시간 
#     if 5<= time <= 15:
#         print("[0] {}번째 손님 (소요시간 : {}분)".format(i,time))
#         cnt += 1
#     else:
#         print("[ ] {}번째 손님 (소요시간 : {}분)".format(i,time))
# print("총 탑승 승객 : ",cnt)