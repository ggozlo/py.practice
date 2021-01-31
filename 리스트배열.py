#____________________________________________________________________________________________________________리스트
#순서를 따지는 객체집합  
subway=[10,20,30] # 배열생성
print(subway) 
subway = ["유재석","강호동","박명수"]
print(subway)
print(subway.index("강호동")) # 특정 배열 내용물의 위치 출력
subway.append("하하") # 배열 추가( 맨 뒤로)
print(subway)
subway.insert(1, "정형돈") #  특정 순서에 배열추가
print(subway)
print(subway.pop()) # 뒤에서부터 배열 제거
print(subway)
subway.append("유재석")
print(subway)
print(subway.count("유재석")) # 배열내 갯수 세기
num_list = [5,3,1,4,2]
num_list.sort()  # 정렬
print(num_list)  # 
num_list.reverse() # 역정렬
print(num_list)  # 
num_list.clear() # 삭제
print(num_list)
mix_list = ["조세호", 20, True]
print(mix_list)
num_list.extend(mix_list) # 배열 합병, 피합병이 뒤로 
print(num_list)