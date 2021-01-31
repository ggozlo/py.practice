#______________________________________________________________________________________________________________________________________continue, break
absent = [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:  # absent 와 student 가 일치할때 
        continue # 조건 충족시 스킵함
    elif student in no_book:
        print("오늘수업 여기까지. {}는 교무실로".format(student))
        break
    print("{}, 책을 읽어봐".format(student))