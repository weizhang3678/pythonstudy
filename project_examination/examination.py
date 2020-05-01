import pymysql
db = pymysql.connect("localhost","root","gyx0519.","examination" )
cursor = db.cursor()

# insert a student
sql = "Insert into tbl_student values(4, 'Wei', 'F', 'Grade 5-3', 38, 'wei.zhang3678@gmail.com', '2257 Hi Rd Oakville')"
try:
    cursor.execute(sql)
    db.commit()
except Exception as err:
    db.rollback()
    print(err)

# query
# fetchone(), fetchall(), rowcount()
cursor.execute('SELECT * FROM tbl_student')
datas = cursor.fetchall()
for row in datas:
    print(row)

db.close()