def send_email_alert(msg):
    import smtplib
    from email.message import EmailMessage

    EMAIL_ADDRESS = "testprojects880@gmail.com"
    EMAIL_PASSWORD = "*********"

    msg_obj = EmailMessage()
    msg_obj.set_content(msg)
    msg_obj['Subject'] = "Street Light Failure Alert"
    msg_obj['From'] = EMAIL_ADDRESS
    msg_obj['To'] = "abunooralsaba@gmail.com"

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg_obj)

