# import smtplib
#
# my_email = "python.udemy.angela@gmail.com"
# password = "okohfhidysmrnlex"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="appbrewerytesting@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )




import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)


date_of_birth = dt.datetime(year=2002, month=8, day=9, hour=4)
print(date_of_birth)