import smtplib

print(" <<<<<< Powered by -> @brokennaruto >>>>>> ")

server = smtplib.SMTP("smtp.gmail.com",587)

server.starttls()

Login_Mail = input("Enter your Mail: ")
Mail_Password = input("Enter Mail Password: ")

server.login(f"{Login_Mail}",f"{Mail_Password}")

if server.connect == True:
    print("Connected")

else:
    print("Incorrect Mail or password")
    exit()

SendMail = input("Reporting Mail: ")

Context = input("Enter the Content for the Mail: ")

Report_Number = int(input("Number of Reports: "))

for i in range(Report_Number):
    server.sendmail(f"{Login_Mail}",f"{SendMail}",Context)

print(Report_Number,"reports done!")