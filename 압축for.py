#______________________________________________________________________________________________________________________________________한줄 for
student = [1,2,3,4,5]
print(student)
student = [i+100 for i in student] # i에다가 student 배열의 값을 하나씩 불러와서 +100 을 반복
print(student)
student = ["아이언맨", "토르", "그루트"]
print(student)
student = [len(i) for i in student]
print(student)
student = ["iron man", "thor", "groot"]
print(student)
student = [i.upper() for i in student]
print(student)