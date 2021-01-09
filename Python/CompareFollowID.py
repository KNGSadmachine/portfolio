import csv

with open("/Library/WebServer/portfolio/Python/username.csv", encoding = "utf-8-sig") as fp:
    user = fp.read().splitlines()

Compare_FollowID = list(range(0))
for i in range(len(user)):
    try:
        with open("/Users/kk/OneDrive/MASTER/MATLAB/FollowIDs/{}.csv".format(user[i]), encoding = "utf-8-sig") as fp:
            User = fp.read().splitlines()
            User = User[0].split(",")
            User = [int(n) for n in User]
            User = sorted(User)
            Compare_FollowID.append(User)
    except FileNotFoundError:
        print("FileNotFoundError : {}".format(user[i]))

# print(len(Compare_FollowID))

Compare_UserName_with_Num = list(range(0))
Compare_UserName_with_Num_Ratio = list(range(0))
Compare = list(range(0))
for i in range(len(user)):
    for j in range(len(user)):
        if i < j:
            Match_Follower = int(len(set(Compare_FollowID[i]) & set(Compare_FollowID[j])))
            Same_Follower_Ratio_ij = Match_Follower / 5000
            # print("{}, {} : {}".format(user[i],user[j],len(set(Compare_FollowID[i]) & set(Compare_FollowID[j]))))
            Compare_UserName_with_Num.append("{}, {} : {}, Ratio : {}".format(user[i],user[j],len(set(Compare_FollowID[i]) & set(Compare_FollowID[j])),Same_Follower_Ratio_ij))
            
            Compare_UserName_with_Num_Ratio.append(user[i])
            Compare_UserName_with_Num_Ratio.append(user[j])
            Compare_UserName_with_Num_Ratio.append(Match_Follower)
            Compare_UserName_with_Num_Ratio.append(Same_Follower_Ratio_ij)
            
            Compare.append("{},{}".format(user[i],user[j]))
            Compare.append(len(set(Compare_FollowID[i]) & set(Compare_FollowID[j])))



with open ("/Users/kk/OneDrive/MASTER/MATLAB/FollowIDs/Compare/{}.csv".format("Compare_UserName_with_Num"), 'w') as f:
    writer = csv.writer(f)
    writer.writerow (Compare_UserName_with_Num)

with open ("/Users/kk/OneDrive/MASTER/MATLAB/FollowIDs/Compare/{}.csv".format("Compare_UserName_with_Num_Ratio"), 'w') as f:
    writer = csv.writer(f)
    writer.writerow (Compare_UserName_with_Num_Ratio)

with open ("/Users/kk/OneDrive/MASTER/MATLAB/FollowIDs/Compare/{}.csv".format("Compare_sample"), 'w') as f:
    writer = csv.writer(f)
    writer.writerow (Compare)

