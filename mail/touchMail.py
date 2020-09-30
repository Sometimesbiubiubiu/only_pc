import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#发生邮箱服务器
smtpserver = 'smtp.qq.com'
#发送用户和密码
user = '542953597@qq.com'
password = 'faauvwaydijkbbje'
#发送邮箱
sender = '542953597@qq.com'
#接收邮箱
receiver = 'zhangjinyu@zoneyet.com'
#发送邮箱主题
subject = 'python test'
#发送附件
sendfile = open('/Users/mac/Downloads/linshi.txt','rb').read()

att = MIMEText(sendfile,'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="cs.txt"'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

#编写HTML类型的邮件正文
# msg = MIMEText('<html><h1>你好！我是python测试邮件！</h1><html>','html','utf-8')
# msg['Subject'] = Header(subject,'utf-8')
# #连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()
