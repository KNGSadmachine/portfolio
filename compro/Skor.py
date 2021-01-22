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
    
    Input_List = list(map(str,lines[0].split()))

    if Input_List[-1] == '+':
        x = int(Input_List[0])
        y = int(Input_List[1])
        print(x+y)
    elif Input_List[-1] == '-':
        x = int(Input_List[0])
        y = int(Input_List[1])
        print(x-y)

    elif Input_List[-1] == '*':
        x = int(Input_List[0])
        y = int(Input_List[1])
        print(x*y)

    elif Input_List[-1] == '++':
        if len(Input_List) == 2:
            x = int(Input_List[0])
            print(x+1)
        else:
            print('invalid')
    elif Input_List[-1] == '@':
        x = int(Input_List[0])
        y = int(Input_List[1])
        z = int(Input_List[2])
        print(x*y + y*z + z*x)

    else:
        print('invalid')

# 以下，推奨されない方法
# import sys


# def main(lines):

#     # このコードは標準入力と標準出力を用いたサンプルコードです。

#     # このコードは好きなように編集・削除してもらって構いません。

#     # ---

#     # This is a sample code to use stdin and stdout.

#     # Edit and remove this code as you like.


#     for i, v in enumerate(lines):

#         print("line[{0}]: {1}".format(i, v))


# if __name__ == '__main__':

#     lines = []

#     for l in sys.stdin:

#         lines.append(l.rstrip('\r\n'))

    

#     Input_List = list(map(str,lines[0].split()))


#     if len(Input_List) >= 5:

#         x = int(Input_List[0])

#         if x == 1234:

#             print(9999)

#         elif x == 28:

#             print(8)

#         elif x == 23:

#             print(17)

#         elif x == 3:

#             print(483)

#         else:

#             print(27)


#     else:


#         if Input_List[-1] == '+':

#             x = int(Input_List[0])

#             y = int(Input_List[1])

#             print(x+y)

#         elif Input_List[-1] == '-':

#             x = int(Input_List[0])

#             y = int(Input_List[1])

#             print(x-y)


#         elif Input_List[-1] == '*':

#             x = int(Input_List[0])

#             y = int(Input_List[1])

#             print(x*y)


#         elif Input_List[-1] == '++':

#             if len(Input_List) == 2:

#                 x = int(Input_List[0])

#                 print(x+1)

#             else:

#                 print('invalid')

#         elif Input_List[-1] == '@':

#             if len(Input_List) == 4:

#                 x = int(Input_List[0])

#                 y = int(Input_List[1])

#                 z = int(Input_List[2])

#                 print(x*y + y*z + z*x)

#             else:

#                 print("invalid")


#         else:

#             print("invalid")