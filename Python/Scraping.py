import twint

c = twint.Config()
c.Username = "GeekTwi"
# c.Search = "fun"
c.Retweets = True
List_Tri = list(range(0))
A = twint.run.Search(c)  #検索実行
List_Tri.append(c)
List_Tri = List_Tri[0].split()
print(List_Tri)