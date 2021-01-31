
#____________________________________________________________________________________________________________퀴즈
from random import *
users = range(1,21)
users = list(users)
shuffle(users)
winners = sample(users,4)
print("""--당첨자 발표--
치킨 당첨자 : {}
커피 당첨자 : {}
--축하합니다--""".format(winners[0], winners[1:]))
