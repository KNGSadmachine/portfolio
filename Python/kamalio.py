import random
import MeCab
kuji = [1,2,3,4,5,100]
a = random.choice(kuji)
if a >=20:
    print("good")
    print(a)
else:
    print("bad!!!")
    import datetime
    print(datetime.datetime.now())
    print(a)

