# 100桁までの数値の入力があった時，先頭が0となる数値以外の最小値を求めよ．
# 例えば2021という入力があったならば出力は1022である．
# 0122が最小だが先頭が０になっているためこれは不適．答えとはならない．
# 1212122が入力された時，出力は1112222でなければならない．

import sys

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
    
    A = list(map(int,lines[0]))

    A = sorted(A)
    if 0 in A:
        Num = sorted(set(A))[1]
        A = sorted(A)
        Fs = A.pop(A.index(Num))
        A.insert(0,Num)

    else:
        A = sorted(A)
        
    A = [str(i) for i in A]
    A = "".join(A)
    print(A)

# 100桁までの数値の入力があった時，先頭が0となる数値以外の最小値を求めよ．
# 例えば2021という入力があったならば出力は1022である．
# 0122が最小だが先頭が０になっているためこれは不適．答えとはならない．
# 1212122が入力された時，出力は1112222でなければならない．