# coding:utf-8
import time
from datetime import datetime, timedelta
import random
from pprint import pprint


# test:w
# dt = (datetime(2015,1,1,0,0,0) + timedelta(days=+364))
# print(time.mktime(dt.timetuple()))

def dates():
    dates = []
    for n in list(range(0,365)):
        # dt = (datetime(2015,1,1,0,0,0) + timedelta(days=+364)).strftime("%Y-%m-%d")
        dates.append((datetime(2015,1,1,0,0,0) + timedelta(days=+n)).strftime("%Y-%m-%d"))
    return dates

OUTPUT_FILE = "TestData.sql"

prefectures = list(range(1,48))
dates = dates()


# 登録するデータの数だけINSERT文を生成
commands = []
for pref_id in prefectures:

    for date in dates:
        pv = random.randint(1,1500)

        commands.append("INSERT INTO user " \
                        "(prefecture_id , pv, access_time)" \
                        "VALUES ({}, {}, '{}');"\
                        .format(pref_id, pv, date))

sqlCommands = "\n".join(commands)

f = open(OUTPUT_FILE, 'w')
f.write(sqlCommands)
f.close()
