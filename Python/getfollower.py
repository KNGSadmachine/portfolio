
import tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)

user = input("「@ユーザー名」を入力してください：")
#followerIDs = api.followers_ids(user)
followerIDs = api.friends_ids(user)

followerDatas = []
for followerID in followerIDs:
    followerData = {}
    data = api.get_user(followerID)
    followerData["Name"] = data.screen_name
    #followerData["Follow"] = data.friends_count
    #followerData["Follower"] = data.followers_count
    #followerData["Description"] = data.description
    #followerData["TweetCount"] = data.statuses_count
    #followerData["created_at"] = data.created_at
    followerDatas.append(followerData)

#import pandas
#表示最大行数
#pandas.set_option("display.max_rows", 1000)
#df = pandas.DataFrame(followerDatas).loc[:,["Name","Follow","Follower","TweetCount","Description"]]

#ファイル出力
#fileName = input("ファイル名を入力してください：")
#df.to_csv(fileName + ".csv")
print(followerDatas)
#print(api.get_user(user))
#from prettyprinter import cpprint # prettyprinterのインポート

#cpprint(api.get_user(user))
