import csv
import numpy as np

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

Compare_Ratio = list(range(0))
Compare = [[]]
for i in range(len(user)):
    for j in range(len(user)):
        Match_Follower = int(len(set(Compare_FollowID[i]) & set(Compare_FollowID[j])))
        Compare[i].append(Match_Follower)
        Same_Follower_Ratio_ij = Match_Follower / 5000
        Compare_Ratio.append(Same_Follower_Ratio_ij)
print(Match_Follower)
try:
    Compare = np.array(Compare).reshape(99, -1)
except ValueError:
    print("Re")

# print(Compare)
# print(Compare)

with open ("/Users/kk/OneDrive/MASTER/MATLAB/FollowIDs/Compare/{}.csv".format("Compare_Heatmap"), 'w') as f:
    writer = csv.writer(f)
    writer.writerow (Compare)
        
