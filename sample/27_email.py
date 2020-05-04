import email.message

msg=email.message.EmailMessage()
# 寄件人
msg["From"]="hmaxiaofei@gmail.com"
# 收件人
msg["To"]="hmaxiaofei@gmail.com"
# 主题
msg["Subject"]="test"
# 内容
msg.set_content("测试")
# html格式送信
# msg.add_alternative("<h3>测试</h3>",subtype="html")

import smtplib
# 建立Gmail服务器连线
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
# 身份验证
server.login("hmaxiaofei@gmail.com","m45x19f865")
# 送信
server.send_message(msg)
# 关闭服务器连接
server.close()