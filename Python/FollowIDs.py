CONSUMER_KEY = "T5jA1etmYE17DdF9L2EJ5q3DC"
CONSUMER_SECRET = "W1hGZhZoCOwgnXFNmAXcgq8rQeny3ygksSaFlAgtEQ2WxSIX8C"
ACCESS_TOKEN = "1268793730032525312-KEsf8qt95wDRlkIp3KCKll3HbjQ5uL"
ACCESS_TOKEN_SECRET = "vWhTwRRQPppaPd0kHoiBZtUqqwGo6JXRrOyxO5qqgHKdA"

import tweepy
import datetime
import csv
import re

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)

Start_time = datetime.datetime.now()
Start_time = str(Start_time)
Start_time = re.split("[-:. ]", Start_time)
Start_time.pop(-1)
Start_time = map(str, Start_time)
Start_time_str = "".join(Start_time)
Start_time = int(Start_time_str)
print(Start_time)

with open("/Library/WebServer/portfolio/Python/username.csv", encoding = "utf-8-sig") as fp:
    user = fp.read().splitlines()

for i in range(37,51,1):
    User = user[i]
    FollowerIDs = api.followers_ids(User)
    print(len(FollowerIDs))
    # FollowerIDs = [str(follower) for follower in FollowerIDs]
    with open ("/Users/kk/OneDrive/MASTER/MATLAB/FollowIDs/{}.csv".format(User), 'w') as f:
        writer = csv.writer(f)
        writer.writerow (FollowerIDs)

End_time = datetime.datetime.now()
End_time = str(End_time)
End_time = re.split("[-:. ]", End_time)
End_time.pop(-1)
End_time = map(str, End_time)
End_time_str = "".join(End_time)
End_time = int(End_time_str)
print(End_time)

# print(sorted(followerIDs))
# followIDs = api.friends_ids(user)

# print(api.get_user(user))

# followerDatas = []
# for followerID in followerIDs:
#     followerData = {}
#     data = api.get_user(followerID)
#     followerData = data.screen_name
#     followerDatas.append(followerData)

# print(followerDatas)

# followDatas = []
# for followID in followIDs:
#     followData = {}
#     data = api.get_user(followID)
#     followData[] = data.screen_name
#     #followerData["Follow"] = data.friends_count
#     #followerData["Follower"] = data.followers_count
#     #followerData["Description"] = data.description
#     #followerData["TweetCount"] = data.statuses_count
#     #followerData["created_at"] = data.created_at
#     followDatas.append(followData)


# #ファイル出力
# #fileName = input("ファイル名を入力してください：")
# #df.to_csv(fileName + ".csv")
# print(user)
# print("FOLLOWER :")
# #print(data.followers_count)
# print(followerDatas)
# print(datetime.datetime.now())
# print("FOLLOW")
# #print(data.friend_count)
# print(followDatas)
# print("END TIME")
# print(datetime.datetime.now())
# #print(api.get_user(user))
# #from prettyprinter import cpprint # prettyprinterのインポート

# #cpprint(api.get_user(user))
