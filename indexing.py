import constants
import functions
import requests
import csv

from requests.packages.urllib3.exceptions import InsecureRequestWarning
from elasticsearch import Elasticsearch, helpers
from datetime import date

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
todayDate = date.today().strftime("%Y-%m-%d")

# Preparing the log file Logger
logName = functions.getLogFileName(todayDate)
loggerNameLog = functions.setup_logger(logName, logName+".log")

# Indicating that the script started
loggerNameLog.critical("[SCRIPT] has started \n")

# To check if error has been commited while bulking
checkLog = True

# Connection to elasticsearch
es = Elasticsearch(constants.ELASTIC_HOST, port=constants.ELASTIC_PORT, verify_certs = constants.VERIFY_CERTS)

loggerNameLog.critical("[CSV] Getting the data from the CSV file \n")
with open('pseudo_facebook.csv') as f:
	reader = csv.DictReader(f)
	loggerNameLog.critical("[CSV] CSV data is ready to be bulked \n")
	bulkRes = helpers.bulk(es, reader, index=constants.ELASTIC_INDEX)

	successBulks = str(bulkRes[0])
	failedBulks = str(len(bulkRes[1]))
	loggerNameLog.critical('[RESULT] : success='+successBulks+' | failed='+failedBulks+ ' \n')
	
	if (not bulkRes[1]):
		loggerNameLog.critical("[END] All data has been bulked successfully \n")
	else :
		checkLog = False
		for failedBulk in bulkRes[1]:
			loggerNameLog.critical("[END FAILED] "+str(failedBulk)+ " has failed \n")

functions.sendEmailNotification(loggerNameLog, checkLog)

loggerNameLog.critical("[SCRIPT] has ended \n")