#______________________________________________________________________________________________________________________________________while
cs = "토르"
index =5
while index >= 1:
    print("{}, 커피가 준비 되었습니다. {}번 남았어요.".format(cs,index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")
cs = "아이언맨"
index = 1
while True: 
    print("{}, 커피가 준비 되었습니다.호출{}회".format(cs,index))
    index +=1
cs = "토르"
person = "Unknown"
while person != cs:
    print("{}, 커피가 준비 되었습니다.".format(cs))
    person = input("이름이 어떻게 되세요? ")