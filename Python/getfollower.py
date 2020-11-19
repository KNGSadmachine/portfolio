CONSUMER_KEY = "T5jA1etmYE17DdF9L2EJ5q3DC"
CONSUMER_SECRET = "W1hGZhZoCOwgnXFNmAXcgq8rQeny3ygksSaFlAgtEQ2WxSIX8C"
ACCESS_TOKEN = "1268793730032525312-KEsf8qt95wDRlkIp3KCKll3HbjQ5uL"
ACCESS_TOKEN_SECRET = "vWhTwRRQPppaPd0kHoiBZtUqqwGo6JXRrOyxO5qqgHKdA"

import tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)

user = input("「@ユーザー名」を入力してください：")
followerIDs = api.followers_ids(user)

followerDatas = []
for followerID in followerIDs:
    followerData = {}
    data = api.get_user(followerID)
    followerData["Name"] = data.name
    followerData["Follow"] = data.friends_count
    followerData["Follower"] = data.followers_count
    #followerData["Description"] = data.description
    followerData["TweetCount"] = data.statuses_count
    followerData["created_at"] = data.created_at
    followerDatas.append(followerData)

#import pandas
#表示最大行数
#pandas.set_option("display.max_rows", 1000)
#df = pandas.DataFrame(followerDatas).loc[:,["Name","Follow","Follower","TweetCount","Description"]]

#ファイル出力
#fileName = input("ファイル名を入力してください：")
#df.to_csv(fileName + ".csv")
#print(followerDatas)
#print(api.get_user(user))
from prettyprinter import cpprint # prettyprinterのインポート

cpprint(api.get_user(user))
