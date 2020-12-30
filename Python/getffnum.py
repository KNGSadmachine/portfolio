
import tweepy
import datetime
import csv
import re

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
Info = list(range(0))
for i in range(len(user)-1):
    User = user[i]
    User_info = api.get_user(User)
    Follower_count = int(User_info.followers_count)
    Follower_num_list.append(User)
    Follower_num_list.append(Follower_count)
    Info.append(User)
    Info.append(User_info)

#終了時間の記述
End_time = datetime.datetime.now()

print(Start_time)
print(End_time)

Start_time = str(Start_time)
Start_time = re.split("[-:. ]", Start_time)
Start_time.pop(-1)
Start_time = map(str, Start_time)
Start_time_str = "".join(Start_time)
Start_time = int(Start_time_str)
print(Start_time)

End_time = str(End_time)
End_time = re.split("[-:. ]", End_time)
End_time.pop(-1)
End_time = map(str, End_time)
End_time_str = "".join(End_time)
End_time = int(End_time_str)
print(End_time)

Follower_num_list.insert(0,Start_time)
Follower_num_list.insert(1,End_time)
Info.insert(0,Start_time)
Info.insert(1,End_time)


with open ("/Users/kk/OneDrive/MASTER/MATLAB/Follow_data/{}.csv".format(End_time), 'w') as f:
    writer = csv.writer(f)
    writer.writerow (Follower_num_list)
with open ("/Users/kk/OneDrive/MASTER/MATLAB/Follow_data/archiveFollowNum.csv", 'a') as f:
    writer = csv.writer(f)
    writer.writerow (Follower_num_list)
with open ("/Users/kk/OneDrive/MASTER/MATLAB/info/{}.csv".format(End_time), 'w',encoding='utf_8_sig') as f:
    writer = csv.writer(f)
    writer.writerow (Info)
with open ("/Users/kk/OneDrive/MASTER/MATLAB/info/archiveInfo.csv", 'a',encoding='utf_8_sig') as f:
    writer = csv.writer(f)
    writer.writerow (Info)

print("Finish")
