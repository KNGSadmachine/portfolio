

with open("/Users/kk/OneDrive/MASTER/MATLAB/FollowIDs/@ariyoshihiroiki.csv", encoding = "utf-8-sig") as fp:
    ariyoshihiroiki = fp.read().splitlines()
    ariyoshihiroiki = ariyoshihiroiki[0].split(",")
    ariyoshihiroiki = [int(n) for n in ariyoshihiroiki]
    ariyoshihiroiki = sorted(ariyoshihiroiki)
# print(ariyoshihiroiki[0])

with open("/Users/kk/OneDrive/MASTER/MATLAB/FollowIDs/@matsu_bouzu.csv", encoding = "utf-8-sig") as fp:
    matsumotohitoshi = fp.read().splitlines()
    matsumotohitoshi = matsumotohitoshi[0].split(",")
    matsumotohitoshi = [int(n) for n in matsumotohitoshi]
    matsumotohitoshi = sorted(matsumotohitoshi)


Count = 0
for i in range(len(ariyoshihiroiki)):
    if ariyoshihiroiki[i] in matsumotohitoshi:
        Count += 1

print(Count)




