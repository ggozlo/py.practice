#__________________________________________________________________________________________________표준 입출력
import sys
print("Python","Java","JavaScript", file=sys.stdout) # 표준출력
print("Python","Java","JavaScript", file=sys.stderr) # 표준오류

scores = {"수학":0,"영어":50,"코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") # l, r정렬 (칸 만큼 확보후) 

for num in range(1,21):
    print("대기번호 : "+str(num).zfill(3)) # .zfill - 공칸을 확보하여 빈공간은 0으로 채움

answer = input("아무 값으나 입력하세요 : ") # input으로 받은값은 항상 str(문자열)

print(type(answer))

print("입력하신 값은" + answer + "입니다.")