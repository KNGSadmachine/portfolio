# import smtplib

# smtp_host = 'smtp.gmail.com'
# smtp_port = 587
# username = 'sansuu716@gmail.com'
# password = ''
# from_address = 'sansuu716@gmail.com'
# to_address = 'sansuu716@gmail.com'
# subject = 'test subject'
# body = 'test body'
# message = ("END")

# smtp = smtplib.SMTP_SSL(smtp_host, smtp_port)
# smtp.login(username, password)
# result = smtp.sendmail(from_address, to_address, message)
# print(result)


lines = 'WU WD RU WD'
B = list(map(str, lines.split()))
print(B)
Ans = [0,0]

for i in range(len(B)-1):
    if B[i] != B[i+1]:
        if B[i] == "WU":
            Ans[0] += 1
        elif B[i] == "WD":
            Ans[0] -= 1
        elif B[i] == "RU":
            Ans[1] += 1
        else:
            Ans[1] -= 1

    if 2 in Ans:
        print("Alice")
        break
    elif -1 in Ans:
        print("Alice")
        break
    else:
        for j in range(len(B)-1):
            if B[j] == B[j+1]:
                print("Alice")
                break
print(Ans)

        

        