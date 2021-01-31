
#__________________________________________________________________________________________________파일 입출력
score_file = open("score.txt", "w", encoding="utf8") # w - 쓰기용, 덮어쓰기
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt","a", encoding="utf8") # a - 이어쓰기 (append)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt","r", encoding="utf8") # r- 읽기용
print(score_file.read()) # 한번에 읽어오기
score_file.close()

score_file = open("score.txt","r", encoding="utf8") # r- 읽기용
print(score_file.readline(), end="") # 줄별로 읽고 커서는 다음줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

while True: # 상시 활성화
    line = score_file.readline() # 한줄씩 읽어서 배열 line 에 저장
    if not line: # 더이상 줄이 없을때(배열 라인에 저장된 값이 없을때) 조건문
        break # 함수 탈출
    print(line, end="")
score_file.close()

score_file = open("score.txt","r", encoding="utf8") # r- 읽기용
lines =score_file.readlines() # list형태로 저장
for line in lines : # 저장된 list에서 한줄씩 line 으로 저장
    print(line, end="")
score_file.close()