import datetime
import json
import pymysql
import requests
import time
import json

creds = json.load(open("creds.json", "r"))
db = pymysql.connect(host=creds["host"],
                     user=creds["user"],
                     password=creds["password"],
                     database=creds["database"])
cursor = db.cursor()


def getCount():
    url = "https://clubconnector.sovd.cloud/api/anwesende/7aa97ff5-a744-4543-9228-8ef4de04ece6-070819/1"
    r = requests.get(url)
    data = json.loads(r.content)
    return int(data["count"])


def getMax():
    url = "https://clubconnector.sovd.cloud/api/anwesende/7aa97ff5-a744-4543-9228-8ef4de04ece6-070819/1"
    r = requests.get(url)
    data = json.loads(r.content)
    return int(data["maxCount"])


c = getCount()
max = getMax()
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
sql = """ INSERT INTO `WalkIn` (count, maxCount, dateTime) VALUES (%s, %s, %s)"""
cursor.execute(sql, (c, max, now))
db.commit()
