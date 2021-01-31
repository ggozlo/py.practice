#__________________________________________________________________________________________________pickle
import pickle

profile_file = open("profile.pickle", "wb",) # 픽클 사용을 위한 b(바이너리) 형식 및 인코딩 불필요
profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
print(profile)

pickle.dump(profile,profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle","rb")
profile = pickle.load(profile_file) # 내용을 불러와서 프로필에 넣음 
print(profile)
profile_file.close()