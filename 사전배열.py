#____________________________________________________________________________________________________________사전
#키값과 연결되는 밸류값을 보관, 키값을 통해 밸류값을 호출 가능함
cabinet = {3:"유재석", 100:"강호동"}
print(cabinet[3]) # 키가 없을때 에러로 프로그램을 종료시킴
print(cabinet[100])
print(cabinet.get(3))  # 키가 없을때 None 값을 출력시키고 코드는 실행시킴
print(cabinet.get(5, "사용가능")) # 키값에 매칭되는 값이 없을때 정해진 결과값 출력
print(3 in cabinet) # 존재여부에 대한 진위판별
cabinet = {"A-3":"유재석", "B-100":"강호동"}
print(cabinet["A-3"])
print(cabinet["B-100"])
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호" # 추가, 이미 존재한다면 덮어씌움
print(cabinet)
del cabinet["A-3"] # 삭제 
print(cabinet)
print(cabinet.keys())  #키값만 출력
print(cabinet.values()) # 밸류만 출력
print(cabinet.items()) # 키,밸류 쌍으로 출력
cabinet.clear() # 삭제
print(cabinet)