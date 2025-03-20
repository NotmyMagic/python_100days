import smtplib
import datetime as dt
import random

my_email = "calepythontest@gmail.com"
my_password = "fdip ymxh dwfr wwiv"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="calepythontest@yahoo.com", msg="Subject:Hello\n\nThis is in my email body")


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("./part4/test/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Week started right\n\n{quote}")