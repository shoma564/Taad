import MySQLdb, request

connection = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='tmcittmcit',
    db='Taad_db',
    charset='utf8'
)


cursor = connection.cursor()
printf("チーム数の入力")
teamnum = input()
printf("チーム名の入力")
for i in range(teamnum):
    teamname = input(teamnum)
    mozi = "INSERT INTO score(teamname) VALUES (" + str(teamname) + ");"
    print(mozi)
    cursor.execute(mozi)
connection.commit()
connection.close()



cursor = connection.cursor()
for i in range(teamnum):
    url = "192.168.20.1" + str(teamnum)
    res = requests.get(url)
    res = str(res)
    print(res.status_code)
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
        print("no response")
    time.sleep(2)

# ポイント閲覧
