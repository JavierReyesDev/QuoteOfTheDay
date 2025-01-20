import smtplib
from random import choice

sender = "" # email to send the email from
recipient_list = [
    # emails to send the email to
]

my_password = "" # application password 

def get_random_message():
    with open("quotes.txt") as file:
        data_lines = file.read().splitlines()
        line = choice(data_lines)
    return line

subject="Cheer up, everything will be fine"
message = get_random_message()

for recipient in recipient_list:
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender, password=my_password)
            connection.sendmail(
                from_addr=sender,
                to_addrs=recipient,
                msg=f"Subject:{subject}\n\n{message}".encode('utf-8')
            )
    except smtplib.SMTPException:
        print("The email could not be sent")
    else:
        print("The email was sent successfully")
