import pandas as pd
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

df = pd.read_csv(r"emails.csv", encoding="utf-8", sep=",")
print(df)


hostMail = "email-address"
password = "password"

def send_message(email, name):
    msg = MIMEMultipart()
    msg["From"] = hostMail
    msg["To"] = email
    msg["Subject"] = "test"

    html_content = f"""
  <!DOCTYPE html>
  <html lang="ar">
    <head>
      <style>
        .title {
            "font-size: 14px;"
            "font-weight: bold;"
            "margin-bottom: 3px;"
        }
        .content {
            "font-size: 12px;"
        }

      </style>
    </head>
    <body dir="rtl">
      <div>
        <p class= "title"> سعادة الأستاذ {name} </p>
        <p class= "title">السلام عليكم ورحمة الله وبركاته</p>
        <p class = "content">
              massage here 
            
        </p>
        <p class= "title"> فريق TEDxKFU</p>
      </div>
      </section>
    </body>
  </html>
"""

    html_part = MIMEText(html_content, "html")
    msg.attach(html_part)

    # with open(r"path", "rb") as image_file:
    #     image_data = image_file.read()

    # image_part = MIMEImage(image_data, name="image.jpg")
    # image_part.add_header("Content-ID", "<image.jpg>")
    # msg.attach(image_part)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as server:
        try:
            server.starttls()
            server.login(hostMail, password)
            server.sendmail(hostMail, email, msg.as_string())
            print("Email sent to", email)
        except Exception as e:
            print("An error occurred while sending the email:", str(email))
            # Store exception in a new CSV file
            error_df = pd.DataFrame({'name':[name],'email': [email]})
            error_df.to_csv('error_log.csv', mode='a', index=False)

for index,row in df.iterrows():
    send_message(row[0], row[1])