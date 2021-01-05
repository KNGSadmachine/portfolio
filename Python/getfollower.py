
import tweepy
import datetime
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit = True)
print("START TIME")
print(datetime.datetime.now())

user = input("「ユーザー名」を入力してください：")
followerIDs = api.followers_ids("@" + user)

print(followerIDs)
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
