import sys
import itertools

Input = list(range(0))
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    for i, v in enumerate(lines):
        Status = v
        Status = Status.split()
        Input.append(Status)

    Lev_M = Input[0]
    Kill = Input[1]
    Spell = Input[2]

    Mon = list(range(int(Lev_M[0]),int(Lev_M[1]) +1,1))
    
    Death = list(range(0))
    for i in range(int(Kill[0])):
        for j in range(int(len(Mon))):
            if int(Mon[j])%int(Spell[i]) == 0:
                Death.append(Mon[j])

    Death = sorted(Death)  
    Death = [str(n) for n in Death] 
    for i in reversed(range(len(Death)-1)): 
        if Death[i] == Death[i+1]:
            del Death[i]

    print(len(Mon) - len(Death))

###################################################

import sys
import itertools
import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

Input = list(range(0))
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    for i, v in enumerate(lines):
        Status = v
        Status = Status.split()
        Input.append(Status)

    Lev_M = [10,724]
    Kill = [3]
    Spell = [7,39,51]

    Lev_M = [int(i) for i in Input[0]]
    Kill = [int(i) for i in Input[1]]
    Spell = [int(i) for i in Input[2]]

    
    Ans = list(range(0))
    Dub = list(range(0))
    if 1 in Spell:
        print(0)
    else:
            
        for i in Spell:
            Can_Kill = (Lev_M[1] - Lev_M[0])//i
            Ans.append(Can_Kill)

        for pair in itertools.combinations(Spell,2):
            Dub.append(pair)
        
        for i in range(len(Dub)-1):
            Not_Kill = (-Lev_M[1] + Lev_M[0])//lcm(Dub[i][0],Dub[i][1])
            Ans.append(Not_Kill)
        #print(Ans)
        if 1 in Kill:
            print(Lev_M[1] - Lev_M[0]  - sum(Ans))
        else:
            print(Lev_M[1] - Lev_M[0] +1 - sum(Ans))

#############################
import sys
import itertools
import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

Input = list(range(0))
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    for i, v in enumerate(lines):
        Status = v
        Status = Status.split()
        Input.append(Status)

    Lev_M = [int(i) for i in Input[0]]
    Kill = [int(i) for i in Input[1]]
    Spell = [int(i) for i in Input[2]]
    Spell = sorted(Spell)
    
    Ans = list(range(0))
    Dub = list(range(0))
    if 1 in Spell:
        print(0)
    elif Lev_M[1] < 1000000:
        Mon = list(range(int(Lev_M[0]),int(Lev_M[1]) +1,1))
    
        Death = list(range(0))
        for i in range(int(Kill[0])):
            for j in range(int(len(Mon))):
                if int(Mon[j])%int(Spell[i]) == 0:
                    Death.append(Mon[j])

        Death = sorted(Death)  
        Death = [str(n) for n in Death] 
        for i in reversed(range(len(Death)-1)): 
            if Death[i] == Death[i+1]:
                del Death[i]

        print(len(Mon) - len(Death))
    else:
        Ans = list(range(0))
        Dub = list(range(0))
        Num = sorted(Spell, reverse=True)
        for i in Spell:
            Can_Kill = (Lev_M[1] - Lev_M[0])//i
            Ans.append(Can_Kill)

        for pair in itertools.combinations(Spell,2):
            Dub.append(pair)
        
        for i in range(len(Dub)-1):
            Not_Kill = (-Lev_M[1] + Lev_M[0])//lcm(Dub[i][0],Dub[i][1])
            Ans.append(Not_Kill)
        #print(Ans)
        if 1 in Kill:
            print(Lev_M[1] - Lev_M[0]  - sum(Ans))
        else:
            print(Lev_M[1] - Lev_M[0] +1 - sum(Ans))

#↑14個正解

# ok 1 [単純なケース] 1以上10以下のレベルの敵がいて、呪文の数が2個であるときに正答できる

# ok 2 [単純なケース] 10以上724以下のレベルの敵がいて、呪文の数が3個であるときに正答できる

# #### 入力:

# 1 9827498525324

# 1

# 1

# #### 標準エラー出力:

# Traceback (most recent call last):

#   File "main.py", line 25, in <module>

#     Mon = list(range(int(Lev_M[0]),int(Lev_M[1]) +1,1))

# MemoryError

# Command exited with non-zero status 1

# not ok 3 [難しいケース] レベル1デスを使える場合に正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# ok 4 [非常に単純なケース] 73718以上97237以下のレベルの敵がいて、呪文の数が1個であるときに正答できる

# ok 5 [非常に単純なケース] 51218以上81205以下のレベルの敵がいて、呪文の数が1個であるときに正答できる

# ok 6 [非常に単純なケース] 58622以上96508以下のレベルの敵がいて、呪文の数が1個であるときに正答できる

# ok 7 [非常に単純なケース] 45474以上93541以下のレベルの敵がいて、呪文の数が1個であるときに正答できる

# ok 8 [非常に単純なケース] 61208以上96004以下のレベルの敵がいて、呪文の数が1個であるときに正答できる

# ok 9 [非常に単純なケース] 81951以上86301以下のレベルの敵がいて、呪文の数が1個であるときに正答できる

# ok 10 [単純なケース] 32964以上73489以下のレベルの敵がいて、呪文の数が8個であるときに正答できる

# ok 11 [単純なケース] 47222以上82749以下のレベルの敵がいて、呪文の数が8個であるときに正答できる

# ok 12 [単純なケース] 13651以上66872以下のレベルの敵がいて、呪文の数が8個であるときに正答できる

# ok 13 [非常に単純なケース] 33184以上37667以下のレベルの敵がいて、呪文の数が1個であるときに正答できる

# ok 14 [単純なケース] 50275以上60700以下のレベルの敵がいて、呪文の数が2個であるときに正答できる

# #### 入力:

# 349451451 614555370

# 8

# 435692 231582 32060 740815 255014 196629 872488 11787

# #### 標準エラー出力:

# Command terminated by signal 9

# not ok 15 [難しいケース] 349451451以上614555370以下のレベルの敵がいて、呪文の数が8個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# #### 入力:

# 541337263 622577470

# 6

# 576613 360451 868408 355962 596267 572204

# #### 標準エラー出力:

# Command terminated by signal 9

# not ok 16 [難しいケース] 541337263以上622577470以下のレベルの敵がいて、呪文の数が6個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# #### 入力:

# 137168453 631003005

# 7

# 334969 942387 857829 299019 47801 97696 924304

# #### 標準エラー出力:

# Traceback (most recent call last):

#   File "main.py", line 25, in <module>

#     Mon = list(range(int(Lev_M[0]),int(Lev_M[1]) +1,1))

# MemoryError

# Command exited with non-zero status 1

# not ok 17 [難しいケース] 137168453以上631003005以下のレベルの敵がいて、呪文の数が7個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# #### 入力:

# 38361988 773523136

# 6

# 85997 303398 962260 552134 590708 4416

# #### 標準エラー出力:

# Traceback (most recent call last):

#   File "main.py", line 25, in <module>

#     Mon = list(range(int(Lev_M[0]),int(Lev_M[1]) +1,1))

# MemoryError

# Command exited with non-zero status 1

# not ok 18 [難しいケース] 38361988以上773523136以下のレベルの敵がいて、呪文の数が6個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# #### 入力:

# 616231201 765406239

# 6

# 131806749 907519657 874221446 489366200 770791633 428247052

# #### 標準エラー出力:

# Command terminated by signal 9

# not ok 19 [難しいケース] 616231201以上765406239以下のレベルの敵がいて、呪文の数が6個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# #### 入力:

# 1903008672 2034206183

# 8

# 240170655 656121840 117114300 252067413 569947507 430041391 107226055 967050976

# #### 標準エラー出力:

# Command terminated by signal 9

# not ok 20 [難しいケース] 1903008672以上2034206183以下のレベルの敵がいて、呪文の数が8個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# #### 入力:

# 6139167 1667661735

# 3

# 289645199 988089057 290409500

# #### 標準エラー出力:

# Traceback (most recent call last):

#   File "main.py", line 25, in <module>

#     Mon = list(range(int(Lev_M[0]),int(Lev_M[1]) +1,1))

# MemoryError

# Command exited with non-zero status 1

# not ok 21 [難しいケース] 6139167以上1667661735以下のレベルの敵がいて、呪文の数が3個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# #### 入力:

# 503912849 2012064484

# 6

# 570556360 952183891 7789439 877218381 720434248 310571220

# #### 標準エラー出力:

# Traceback (most recent call last):

#   File "main.py", line 25, in <module>

#     Mon = list(range(int(Lev_M[0]),int(Lev_M[1]) +1,1))

# MemoryError

# Command exited with non-zero status 1

# not ok 22 [難しいケース] 503912849以上2012064484以下のレベルの敵がいて、呪文の数が6個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# #### 入力:

# 1 1000000000000000000

# 10

# 485278786 917367266 477606006 635986203 914812984 107918120 112248576 302815519 398749321 402524265

# #### 標準エラー出力:

# Traceback (most recent call last):

#   File "main.py", line 25, in <module>

#     Mon = list(range(int(Lev_M[0]),int(Lev_M[1]) +1,1))

# MemoryError

# Command exited with non-zero status 1

# not ok 23 [難しいケース] 1以上1000000000000000000以下のレベルの敵がいて、呪文の数が10個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# #### 入力:

# 1 1000000000000000000

# 10

# 48 84 96 56 10 99 5 66 31 45

# #### 標準エラー出力:

# Traceback (most recent call last):

#   File "main.py", line 25, in <module>

#     Mon = list(range(int(Lev_M[0]),int(Lev_M[1]) +1,1))

# MemoryError

# Command exited with non-zero status 1

# not ok 24 [難しいケース] 1以上1000000000000000000以下のレベルの敵がいて、呪文の数が10個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# #### 入力:

# 1 1000000000000000000

# 10

# 14229 95312 10929 77890 6152 78286 32557 70111 67946 99793

# #### 標準エラー出力:

# Traceback (most recent call last):

#   File "main.py", line 25, in <module>

#     Mon = list(range(int(Lev_M[0]),int(Lev_M[1]) +1,1))

# MemoryError

# Command exited with non-zero status 1

# not ok 25 [難しいケース] 1以上1000000000000000000以下のレベルの敵がいて、呪文の数が10個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# #### 入力:

# 1 1000000000000000000

# 10

# 29516 34882 63315 28983 7176 96533 33422 84834 43803 61310

# #### 標準エラー出力:

# Traceback (most recent call last):

#   File "main.py", line 25, in <module>

#     Mon = list(range(int(Lev_M[0]),int(Lev_M[1]) +1,1))

# MemoryError

# Command exited with non-zero status 1

# not ok 26 [難しいケース] 1以上1000000000000000000以下のレベルの敵がいて、呪文の数が10個であるときに正答できる

#   AssertionError: ステータスコードが正常(0)ではありません

#       at TestRunner.verifyStatusCode (/root/node_modules/codecheck/src/test_runner/testRunner.js:130:14)

#       at processTicksAndRejections (internal/process/task_queues.js:97:5)

#       at async TestRunner.postProcess (/root/node_modules/codecheck/src/test_runner/testRunner.js:105:5)

#       at async Context.<anonymous> (/root/node_modules/codecheck/src/test_runner/testRunner.js:95:9)

# # tests 26

# # pass 13

# # fail 13

# exit_code = 13, reason = DONE

