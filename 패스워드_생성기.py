
#____________________________________________________________________________________________________________문제
site = "http://naver.com"
del_str = site.replace("http://", "")
print(del_str)
main_str = del_str[:del_str.index(".")]
print(main_str)
password =main_str[0:3]+str(len(main_str))+str(main_str.count("e"))+"!"
print(f"{site}의 패스워드는 {password}입니다.")