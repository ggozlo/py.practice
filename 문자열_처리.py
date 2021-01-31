# ____________________________________________________________________________________________________________ 문자열 처리함수
python = "Python is Amazingnnnnnnnnnnnn"
print(python.lower()) # 전체 소문자출력
print(python.upper()) # 전체 대문자출력
print(python[0].isupper()) # 대문자인지 진위여부 파악
print(len(python)) # 문자열 길이 
print(python.replace("Python", "Java"))  # 문자열에서 특정내용을 변경
index = python.index("n") # 특정문자 위치 검색 
print(index)
index = python.index("n", index + 1 ) # 다음순번 검색
print(index)
print(python.find("is")) # 검색기능, 출력값을 참, 거짓
print(python.count("n")) # 카운트