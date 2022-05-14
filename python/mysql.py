import MySQLdb, requests, time

connection = MySQLdb.connect(host='192.168.2.2',user='root',passwd='tmcit',db='Taad_db',charset='utf8')
iplist = ['192.168.60.12', '192.168.60.22', '192.168.60.32', '192.168.60.253']

cursor = connection.cursor()
print("チーム数の入力")
teamnum = input()
teamnum = int(teamnum)
print("チーム名の入力")
for i in range(teamnum):
    teamname = input(str(teamnum) + ">>>>")
    mozi = "INSERT INTO score(teamname) VALUES (\'" + str(teamname) + "\');"
    print(mozi)
    cursor.execute(mozi)
connection.commit()
connection.close()


while True:
    cursor = connection.cursor()
    for na in iplist:
        url = na
        try:
            print(url)
            res = requests.get(url)
            res = str(res)
            if res == "200":
                print("ポイント追加")
                mozi = "SELECT * FROM score WHERE id =" + str(teamnum) + ";"
                cursor.execute(mozi)
                rows = cursor.fetchall()
                rows = int(rows) + 10
                print(rows)
                mozi = "INSERT INTO score(rows) VALUES (" + str(rows) + ");"
                cursor.execute(mozi)
            else:
                print("bad request")
        except:
            print("no response")
        time.sleep(2)

# ポイント閲覧
