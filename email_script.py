import requests
import json
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

def get_json(url):
	req = requests.get(ur)
	data= json.loads(req.text)
	return data

def send_email():
	sender = "techworldstarzllc@gmail.com"
	msg = MIMEText("Here is the body of the message")
	msg["From"] = sender
	msg["To"] = "edgar.factorial@gmail.com"
	msg["Subject"] = "A test case"
	p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
	p.communicate(msg.as_bytes())
	print("Running")


if __name__ == "__main__":
	#print("Hello")
	send_email()