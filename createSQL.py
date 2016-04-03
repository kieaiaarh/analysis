# coding:utf-8
import random
import time
from datetime import datetime

print time.strftime(format, time.localtime)

def prefecture_ids():
    return prefs = [1..47]

def randomAge():
    return random.randint(1, 1200)

# startからendの間でランダムな日付生成
def randomDate(start, end):
    format = '%Y-%m-%d %H:%M:%S'
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + random.random() * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

# 出力するファイル名
OUTPUT_FILE = "TestData.sql"

# 登録するデータ件数
RECORD_COUNT = 10

# 実行するSQLコマンド文字列
sqlCommands = ""

# 使用するデータベースを指定(今回はCreateTestData)
sqlCommands += "USE CreateTestData;\n"

# 登録するデータの数だけINSERT文を生成
for _ in range(RECORD_COUNT):

    # 登録するランダムなデータの生成
    name = randomName()
    age  = randomAge()
    date = randomDate("2014-6-28 00:00:00", "2015-6-28 00:00:00")

    # ランダムなデータからInsert文を生成
    sqlCommands += "INSERT INTO user " \
                    "(prefecture_id , pv, access_time)" \
                    "VALUES ('{}', '{}', '{}');\n"\
                    .format(name, age, date)

# 生成したSQLコマンドをファイルに書き出す
f = open(OUTPUT_FILE, 'w')
f.write(sqlCommands)
f.close()
