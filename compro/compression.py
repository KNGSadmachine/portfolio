# s = 'AAAAAA' => 6A
# s = 'ABAAAC' => -2AB3A-1C
# このようなsの入力があった場合，出力は=>のようになる．アルゴリズムを考えよ．
# また，逆変換をするようなアルゴリズムを考えよ．

import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

# # def comp(lines):
#         A = v[2]
#         for i in range(len(A)):
#             print(A)
    

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    for i, v in enumerate(lines):
        #print("{}".format(v))
    #v = 'compress ABAAACC'
        B = v
    B = B.split()

    Cnt_same = 1
    Cnt_not = 1

    Ans = list(range(0))
    if B[0] == "compress":
        C = list(map(str,B[1]))
        for i in range(len(C)-1):
            if C[i] == C[i+1]:
                if Cnt_not >= 2:
                    Ans.append(-(Cnt_not -1))
                    for k in range(i - Cnt_not +1, i,1):
                        Ans.append(C[k])
                    Cnt_not = 1
                Cnt_same += 1
            else:
                if Cnt_same >= 2:
                    Ans.append(Cnt_same)
                    Ans.append(C[i-1])
                    Cnt_same = 1
                Cnt_not += 1
            #print(Cnt_same)
            #print(Cnt_not)
            if i == len(C) -2:
                if Cnt_same >= 2:
                    Ans.append(Cnt_same)
                    Ans.append(C[i-1])
                else:
                    if Cnt_not >= 2:
                        Ans.append("-1")
                        Ans.append(C[i+1])

                        
    Ans = map(str, Ans)
    G = "".join(Ans)
    print(G)
    #print(Cnt_not)
    #print("{0}{1}".format(Cnt_same,"A"))