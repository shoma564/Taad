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


while True:
    pop = 1
    for na in iplist:
        url = "http://" + str(na) + ":80"
        try:
            print(url)
            res = requests.get(url)
            res = str(res)
            print(res)

            if res == "<Response [200]>":
                print("ポイント追加")
                mozi = "SELECT score FROM score WHERE id =" + str(pop) + ";"
                cursor.execute(mozi)
                rows = cursor.fetchall()
                rows = str(rows)
                rows = (rows.replace('(', ''))
                rows = (rows.replace(')', ''))
                rows = (rows.replace(',', ''))
                rows = int(rows)
                rows = int(rows) + 10
                print(rows)
                mozi = "update score set score=" + str(rows) + " where id =" + str(pop) + ";"
                cursor.execute(mozi)
                connection.commit()
            else:
                print("bad request")
        except:
            print("no response")
        pop = pop + 1
        time.sleep(1)

# ポイント閲覧
