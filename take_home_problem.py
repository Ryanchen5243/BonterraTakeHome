import requests
import csv
import os
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

API_ENDPOINT = "https://api.myngp.com/v2/broadcastEmails"
api_key = os.environ.get('API_KEY')
user_name = os.environ.get('USER_NAME')

# Define CSV file path
CSV_FILE_PATH = "EmailReport.csv"


emailData = {} # dictionary keys are email message id

# fetch data from api
def getDataFromAPI():
    response = requests.get(API_ENDPOINT,auth = HTTPBasicAuth(user_name,api_key))
    data = response.json()
    numEntries = data.get('count')
    for i in range(numEntries): # loop through emails
        messageID = data.get('items')[i].get('emailMessageId')
        name = data.get('items')[i].get('name')
        # print(str(messageID) + " "+ name)
        # print("----------------------------------------")
        d1 = requests.get("https://api.myngp.com/v2/broadcastEmails/{emailMessageId}?$expand=statistics".format(emailMessageId=messageID),
                          auth = HTTPBasicAuth(user_name,api_key)).json()
        # print("top line stats for this email:")
        # print(d1['statistics'])
        currStats = d1['statistics']
        emailData[messageID] = {"emailName": name,
                "recipients": currStats['recipients'],
                "opens":currStats['opens'],
                "clicks":currStats['clicks'],
                "unsubs":currStats['unsubscribes'],
                "bounces":currStats['bounces'],
                "topVariant": None
            }
        # print("---------------------------")
        # print("variants are listed below: ")
        topVariant = None
        topOpenCount = -1
        for my_dict in d1['variants']:
            emailMessageVariantId = my_dict['emailMessageVariantId']
            d2 = requests.get("https://api.myngp.com/v2/broadcastEmails/{emailMessageId}/variants/{emailMessageVariantId}?$expand=statistics".format(emailMessageId=messageID,emailMessageVariantId=emailMessageVariantId),
                         auth=HTTPBasicAuth(user_name,api_key)).json()

            if(d2['statistics']['opens'] > topOpenCount):
                topOpenCount = d2['statistics']['opens']
                topVariant = d2['name']
                emailData[messageID]["topVariant"] = topVariant # update top variant

        if(topVariant is None or topOpenCount == -1):
            raise Exception("Could not locate top performing variant")

def writeToCSV():
    # print(emailData)
    # CSV Headers
    headers = ["Email Message ID", "Email Name", "Recipients", "Opens", "Clicks", "Unsubscribes", "Bounces", "Top Variant"]

    # sort email data by email message id
    sortedEmailData = dict(sorted(emailData.items(), reverse=True))
    # Write Data
    with open(CSV_FILE_PATH, mode="w", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for key,value in sortedEmailData.items():
            writer.writerow({
                "Email Message ID": key,
                "Email Name": value['emailName'],
                "Recipients": value['recipients'],
                "Opens": value['opens'],
                "Clicks": value['clicks'],
                "Unsubscribes": value['unsubs'],
                "Bounces": value['bounces'],
                "Top Variant": value['topVariant']
            })

# write data to csv file
def main():
    getDataFromAPI()
    writeToCSV()
    print("Email report complete, file is {name}".format(name=CSV_FILE_PATH))

if __name__ == "__main__":
    main()