#__________________________________________________________________________________________________기본값
def profile(name, age , main_lang):
    print("이름 : {}\t나이 : {}\t주 사용 언어 : {}"\
        .format(name, age, main_lang))
profile("유재석",20,"파이썬")
profile("김태호",25,"자바")

def profile(name="강백호", age=17 , main_lang="파이썬"):
    print("이름 : {}\t나이 : {}\t주 사용 언어 : {}"\
        .format(name, age, main_lang))
profile("유재석")
profile("조혜련")