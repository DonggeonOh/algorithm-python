import pickle

# pickle 쓰기
profile_pickle = open('profile.pickle', 'wb')  # b - binary 를 의미
profile = {"이름":"오동건", "나이":26, "취미":["게임", "키보드", "코딩"]}
pickle.dump(profile, profile_pickle)  # profile 에 있는 정보를 file에 저장한다.
profile_pickle.close()


# pickle 읽기
profile_pickle = open('profile.pickle', 'rb')
profile = pickle.load(profile_pickle)
print(profile)
profile_pickle.close()


# with 도 있지만 생략한다