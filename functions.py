import logging
import constants
import smtplib

#To setup as many loggers as you want
def setup_logger(name, log_file, loggerType = 'other', level=logging.INFO):
    if (loggerType != 'backup'): 
        formatter = logging.Formatter('%(asctime)s [INFO] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        
    handler = logging.FileHandler(log_file)

    if (loggerType != 'backup'): 
        handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def getLogFileName(todayDate):
    logName = constants.log_folder+constants.log_file+todayDate
    return logName

def sendEmailNotification(loggerNameLog, status):
	gmail_user = constants.GMAIL_USER
	gmail_password = constants.GMAIL_PASSWORD

	sent_from = gmail_user
	to = constants.GMAIL_TO
	subject = constants.SUBJECT
	if (status == True):
		body = 'The csv data has been imported successfully'
	else :
		body = 'Check the CSV LOG some references has failed'

	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)

	try:
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(sent_from, to, email_text)
		server.close()

		loggerNameLog.critical("[EMAIL] sent! \n")
	except:
		loggerNameLog.critical("[EMAIL] Failed to send \n")