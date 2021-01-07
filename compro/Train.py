import sys
import datetime

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    for i, v in enumerate(lines):
        print("line[{0}]: {1}".format(i, v))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    R, S, DIR, HH = lines[0].split()
    #R = str(R)
    A1_A7_H = list(range(0))
    A1_A7_M = list(range(0))
    A1_A7_T = datetime.datetime(2020,1,1,5,50,0)
    A1_A13_H = list(range(0))
    A1_A13_M = list(range(0))

    A7_A1_H = list(range(0))
    A7_A1_M = list(range(0))
    A7_A1_T = datetime.datetime(2020,1,1,5,56,0)
    A7_A13_H = [6]
    A7_A13_M = [10]
    A13_A1_H = list(range(0))
    A13_A1_M = list(range(0))
    A13_A1_T = datetime.datetime(2020,1,1,5,42,0)
    A13_A7_H = [22]
    A13_A7_M = [52]

    B1_A7_H = list(range(0))
    B1_A7_M = list(range(0))
    B1_A7_T = datetime.datetime(2020,1,1,5,54,0)
    A7_B1_H = list(range(0))
    A7_B1_M = list(range(0))
    A7_B1_T = datetime.datetime(2020,1,1,6,5,0)
    Time_A_U = [0,3,8,10,13,17,20]
    Time_A_D = [0,3,7,10,12,17,20]
    Time_B_U = [0,4,7,10,12,15]
    Time_B_D = [0,3,5,8,11,15]
    Fs_num = list(range(0))
    Sc_num = list(range(0))
    B1_num = list(range(0))
    B2_num = list(range(0))
    Ans = list(range(0))
    Bf = list(range(0))

    Num = int(S[1])
    if R in "A":
        for i in range(204):
            A1_A7_T = A1_A7_T + datetime.timedelta(minutes=5)
            if i%2 == 0:
                A1_A7_H.append(A1_A7_T.strftime("%H"))
                A1_A7_M.append(A1_A7_T.strftime("%M"))
            else:
                A1_A13_H.append(A1_A7_T.strftime("%H"))
                A1_A13_M.append(A1_A7_T.strftime("%M"))
        # print(A1_A13_H)
        # print(A1_A13_M)
        for i in range(102):
            A7_A1_T = A7_A1_T + datetime.timedelta(minutes=10)
            A7_A1_H.append(A7_A1_T.strftime("%H"))
            A7_A1_M.append(A7_A1_T.strftime("%M"))

        for i in range(102):
            A13_A1_T = A13_A1_T + datetime.timedelta(minutes=10)
            A13_A1_H.append(A13_A1_T.strftime("%H"))
            A13_A1_M.append(A13_A1_T.strftime("%M"))
        
        # print(len(A7_A1) == len(A1_A7))
        A1_A7_H = [int(s) for s in A1_A7_H]
        A1_A7_M = [int(s) for s in A1_A7_M]
        A1_A13_H = [int(s) for s in A1_A13_H]
        A1_A13_M = [int(s) for s in A1_A13_M]
        A7_A1_H = [int(s) for s in A7_A1_H]
        A7_A1_M = [int(s) for s in A7_A1_M]
        A13_A1_H = [int(s) for s in A13_A1_H]
        A13_A1_M = [int(s) for s in A13_A1_M]
        # print(A1_A13_H)
        

      

        if 1 < Num < 7:
            if DIR == "U":
                for i in range(len(A1_A7_H)):
                    if A1_A7_H[i] == int(HH):
                        Fs_num.append(i)
                    elif A1_A7_H[i] == int(HH)-1 and A1_A7_H[i] > 6:
                        B1_num.append(i)

                for i in range(len(A1_A13_H)):
                    if A1_A13_H[i] == int(HH):
                        Sc_num.append(i)
                    elif A1_A13_H[i] == int(HH)-1 and A1_A13_H[i] > 6:
                        B2_num.append(i)

                for i in Fs_num:
                    Ans.append(A1_A7_M[i]+Time_A_U[Num - 1])
                for i in Sc_num:
                    Ans.append(A1_A13_M[i]+Time_A_U[Num - 1])
                for i in B1_num:
                    Bf.append(A1_A7_M[i]+Time_A_U[Num - 1]-60)
                for i in B2_num:
                    Bf.append(A1_A13_M[i]+Time_A_U[Num - 1]-60)
            
            else:
                for i in range(len(A7_A1_H)):
                    if A7_A1_H[i] == int(HH):
                        Fs_num.append(i)
                    elif A7_A1_H[i] == int(HH)-1 and A7_A1_H[i] > 6:
                        B1_num.append(i)

                for i in range(len(A13_A1_H)):
                    if A13_A1_H[i] == int(HH):
                        Sc_num.append(i)
                    elif A13_A1_H[i] == int(HH)-1 and A13_A1_H[i] > 6:
                        B2_num.append(i)
                

                for i in Fs_num:
                    Ans.append(A7_A1_M[i]+Time_A_D[Num - 1])
                for i in Sc_num:
                    Ans.append(A13_A1_M[i]+Time_A_D[Num - 1])

                for i in B1_num:
                    Bf.append(A7_A1_M[i]+Time_A_D[Num - 1]-60)

                for i in B2_num:
                    Bf.append(A13_A1_M[i]+Time_A_D[Num - 1]-60)


        else:
            if DIR == "U":
                for i in range(len(A7_A13_H)):
                    if A7_A13_H[i] == int(HH):
                        Fs_num.append(i)
                    elif A7_A13_H[i] == int(HH)-1:
                        B1_num.append(i)

                for i in range(len(A1_A13_H)):
                    if A1_A13_H[i] == int(HH):
                        Sc_num.append(i)
                    elif A1_A13_H[i] == int(HH)-1:
                        B2_num.append(i)

                for i in Fs_num:
                    Ans.append(A7_A13_M[i]+Time_A_U[Num - 1])
                for i in Sc_num:
                    Ans.append(A1_A13_M[i]+Time_A_U[Num - 1])
                for i in B1_num:
                    Bf.append(A7_A13_M[i]+Time_A_U[Num - 1]-60)
                for i in B2_num:
                    Bf.append(A1_A13_M[i]+Time_A_U[Num - 1]-60)

            else:
                for i in range(len(A13_A7_H)):
                    if A13_A7_H[i] == int(HH):
                        Fs_num.append(i)
                    elif A13_A7_H[i] == int(HH)-1:
                        B1_num.append(i)

                for i in range(len(A13_A1_H)):
                    if A13_A1_H[i] == int(HH):
                        Sc_num.append(i)
                    elif A13_A1_H[i] == int(HH)-1:
                        B2_num.append(i)

                for i in Fs_num:
                    Ans.append(A13_A7_M[i]+Time_A_D[Num - 1])
                for i in Sc_num:
                    Ans.append(A13_A1_M[i]+Time_A_D[Num - 1])
                for i in B1_num:
                    Bf.append(A13_A7_M[i]+Time_A_D[Num - 1]-60)
                for i in B2_num:
                    Bf.append(A13_A1_M[i]+Time_A_D[Num - 1]-60)
#


    else:
        for i in range(169):
            A7_B1_T = A7_B1_T + datetime.timedelta(minutes=6)
            A7_B1_H.append(A7_B1_T.strftime("%H"))
            A7_B1_M.append(A7_B1_T.strftime("%M"))

        for i in range(len(A7_B1_H)):
            B1_A7_T = B1_A7_T + datetime.timedelta(minutes=6)
            B1_A7_H.append(B1_A7_T.strftime("%H"))
            B1_A7_M.append(B1_A7_T.strftime("%M"))
        
        if DIR == "U":
            for i in range(len(B1_A7_H)):
                if A1_A7_H[i] == int(HH):
                    Fs_num.append(i)
                elif A1_A7_H[i] == int(HH)-1:
                    B1_num.append(i)

            for i in Fs_num:
                Ans.append(B1_A7_M[i]+Time_B_U[Num - 1])
            for i in B1_num:
                Bf.append(B1_A7_M[i]+Time_B_U[Num - 1]-60)
            
        else:
            for i in range(len(A7_B1_H)):
                if A7_A1_H[i] == int(HH):
                    Fs_num.append(i)
                elif A7_A1_H[i] == int(HH)-1:
                    B1_num.append(i)

            for i in Fs_num:
                Ans.append(A7_B1_M[i]+Time_B_D[Num - 1])
            for i in B1_num:
                Bf.append(A7_B1_M[i]+Time_B_D[Num - 1]-60)

        # print(len(A7_B1) == len(B1_A7))
    if Ans != []:
        for i in Bf:
            if i > 0:
                Ans.append(i)
        Ans = [h for h in Ans if h < 60]
        Ans = sorted(Ans)
        Ans = [str(s).zfill(2) for s in Ans]
        #print(Ans)
        print("{}:".format(HH),*Ans)
    else:
        print("No train")


