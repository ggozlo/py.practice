#__________________________________________________________________________________________________가변인자
def profile(name, age, *language):
    print("이름:{}\t나이:{}\t".format(name,age), end="") # end - 끝날때 자동줄넘김이 아닌 엔드의 내용으로 대체
    for lang in language:
        print(lang, end=" ")
    print()
profile("유재석",20,"파이선","자바","C","C++","C#","GO")
profile("김테호",25,"코틀린","스위프트","","","")