import requests
import json
import email

def get_json(url):
	req = requests.get(ur)
	data= json.loads(req.text)
	return data

	#bitstamp_api ="http://www.bitstamp.net/api/ticker/"
	#print data

import smtplib
from email.mime.text import MIMEText
fb = open( textfile , 'rb')
msg = MIMEText(fp.read())
fp.close()
msg ['subject'] = 'the contents of %s' % textfile
msg ['from'] = "http://www.bitstamp.net/apli/ticker/"
msg ['to'] = techworldstarzllc@gmail.com
s= smtplib.SMTP('localhost')
s.sendmail(me , [you], msg.as_string())
s.quite
	