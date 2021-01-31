#__________________________________________________________________________________________________표준 입출력
# import sys
# print("Python","Java","JavaScript", file=sys.stdout) # 표준출력
# print("Python","Java","JavaScript", file=sys.stderr) # 표준오류
# scores = {"수학":0,"영어":50,"코딩":100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # l, r정렬 (칸 만큼 확보후) 
# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3)) # .zfill - 공칸을 확보하여 빈공간은 0으로 채움
# answer = input("아무 값으나 입력하세요 : ") # input으로 받은값은 항상 str(문자열)
# print(type(answer))
# print("입력하신 값은" + answer + "입니다.")
#__________________________________________________________________________________________________출력 포맷
# #빈 자리 빈공간, 우정렬 
# print("{0:>10}".format(500))
# # 양수일땐 +표시, 음수 일땐 -로 표시 
# print("{0:>+10}".format(500))
# print("{0:>+10}".format(-500))
# #왼쪽정령, 빈칸 _ 로 채움
# print("{0:_<+10}".format(500))
# # 3자리 마다 콤마 찍기
# print("{0:,}".format(100000000000000))
# # 3자리 마다 콤마 찍기 +- 부호도
# print("{0:+,}".format(100000000000000))
# # 3자리 마다 콤마 찍기, 부호 , 자릿수 확보, 빈자리는^
# print("{0:^<+30,}".format(100000000))
# # 소숫점
# print("{0:f}".format(5/3))
# # 소숫점 특정자리수 까지만
# print("{0:.2f}".format(5/3))
#__________________________________________________________________________________________________파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") # w - 쓰기용, 덮어쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()
# score_file = open("score.txt","a", encoding="utf8") # a - 이어쓰기 (append)
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()
# score_file = open("score.txt","r", encoding="utf8") # r- 읽기용
# print(score_file.read()) # 한번에 읽어오기
# score_file.close
# score_file = open("score.txt","r", encoding="utf8") # r- 읽기용
# print(score_file.readline(), end="") # 줄별로 읽고 커서는 다음줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()
# score_file = open("score.txt","r", encoding="utf8") # r- 읽기용
# while True: # 상시 활성화
#     line = score_file.readline() # 한줄씩 읽어서 배열 line 에 저장
#     if not line: # 더이상 줄이 없을때(배열 라인에 저장된 값이 없을때) 조건문
#         break # 함수 탈출
#     print(line, end="")
# score_file.close()
# score_file = open("score.txt","r", encoding="utf8") # r- 읽기용
# lines =score_file.readlines() # list형태로 저장
# for line in lines : # 저장된 list에서 한줄씩 line 으로 저장
#     print(line, end="")
# score_file.close()
#__________________________________________________________________________________________________pickle
# import pickle
# profile_file = open("profile.pickle", "wb",) # 픽클 사용을 위한 b(바이너리) 형식 및 인코딩 불필요
# profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile,profile_file)  # profile에 있는 정보를 file에 저장
# profile_file.close()
# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file) # 내용을 불러와서 프로필에 넣음 
# print(profile)
# profile_file.close()
#___________________________________________________________________________________________________with(닫기 불필요)
# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))
# with open("study.txt","w",encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")
# with open("study.txt","r",encoding="utf8") as study_file:
#     print(study_file.read())
#___________________________________________________________________________________________________퀴즈
# num = range(1, 51)
# for txt in num : 
#     report_file = open("{}주차.txt".format(txt),"w",encoding="utf8")
#     print("- {} 주차 주간보고 -".format(num), file= report_file)
#     print("부서 :", file= report_file)
#     print("이름 :", file= report_file)
#     print("업무 요약 :", file= report_file)
#     report_file.close
# for i in range(1, 51):
#     with open(str(i) + "주차.txt","w", encoding="utf8") as report_file:
#         report_file.write("- {} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")

