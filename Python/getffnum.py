

import tweepy
import datetime
import csv
import pprint
#import pandas as pd

#魔法の言葉
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)

#開始時間の記述
Start_time = datetime.datetime.now()

with open("/Library/WebServer/portfolio/Python/username.csv", encoding = "utf-8-sig") as fp:
    user = fp.read().splitlines()

#フォロワー数TOP100ユーザーのフォロワー数の取得
Follower_num_list = list(range(0))
for i in range(len(user)-1):
    User = user[i]
    User_info = api.get_user(User)
    print(User_info)
    Follower_count = int(User_info.followers_count)
    #print(User)
    #print(Follower_count)
    Follower_num_list.append(User)
    Follower_num_list.append(Follower_count)

#終了時間の記述
End_time = datetime.datetime.now()

Follower_num_list.insert(0,Start_time)
Follower_num_list.insert(1,End_time)

print(Start_time)
print(End_time)
#print(Follower_num_list)

# with open ("/Users/sadmachine/OneDrive/MASTER/MATLAB/{}.csv".format(End_time), 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow (Follower_num_list)
# print("Finish")