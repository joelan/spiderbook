
import sqlite3
import threading

mutex = threading.Lock()
def  addbookinfo(id,name,cover,author,intro,type):
  conn = sqlite3.connect('book.db')
  # print ("book database successfully")

  c = conn.cursor()

  c.execute("DELETE from bookinfo where bookid='%s'" %(id))

  conn.commit()
  c.execute("INSERT INTO bookinfo  (bookid,name,cover,author,intro,booktype) VALUES ('%s', '%s', '%s', '%s','%s','%s' ) " %(id,name,cover,author,intro,type));
  conn.commit()
  print ("addbookinfo created successfully");
  conn.close()

def addchapters(book,chapter,title,link,file):

  conn = sqlite3.connect('book.db')
  # print("book database successfully")
  c = conn.cursor()
  c.execute("DELETE from BookChapters where bookid='%s'and chapterid='%d'" % (book,chapter))

  c.execute(
    "INSERT INTO BookChapters  (bookid,chapterid,chaptertitle,chapterlink,filename) VALUES ('%s', '%d', '%s', '%s','%s')" %(book,chapter,title,link,file));
  conn.commit()
  print("addchapters created successfully");
  conn.close()

# import pymysql  # 导入 pymysql
#
# # 打开数据库连接
# db=pymysql.connect(host='127.0.0.1', user='mysuer', passwd='223344', db='crazyjoeblog',charset='utf8')
# # db = pymysql.connect("localhost","root","577jl1?;","crazyjoeblog" )
# # 使用cursor()方法获取操作游标
# cur = db.cursor()
#
# # 1.查询操作
# # 编写sql 查询语句  user 对应我的表名
# sql = "SELECT * FROM article"
# try:
#     cur.execute(sql)  # 执行sql语句
#
#     results = cur.fetchall()  # 获取查询的所有记录
#     print("id", "name", "password \n")
#     # 遍历结果
#     for row in results:
#         id = row[0]
#         name = row[1]
#         password = row[2]
#         print(id, name, password)
# except Exception as e:
#     raise e
# finally:
#     db.close()  # 关闭连接

# import pymysql.cursors
# # sql=r"CREATE TABLE 'users' " \
# #     "('id' int(11) NOT NULL AUTO_INCREMENT,'email' varchar(255) COLLATE utf8_bin NOT NULL,'password' varchar(255)" \
# #     " COLLATE utf8_bin NOT NULL,PRIMARY KEY ('id')) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_binAUTO_INCREMENT=1"
#
# def  togetData():
#
#       # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='crazyjoeblog', charset='utf8')
#       conn = pymysql.connect(host='localhost',
#                                    user='root',
#                                    password='123456',
#                                    db='crazyjoeblog',
#                                   port='3306',
#                                    charset='utf8')
#
#       # 创建游标
#       cursor = conn.cursor()
#
#       # 执行SQL，并返回收影响行数
#       effect_row = cursor.execute("SELECT * FROM crazyjoeblog.article")
#
#       row= cursor.fetchall()
#       # 执行SQL，并返回受影响行数
#       # effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))
#
#       # 执行SQL，并返回受影响行数,执行多次
#       # effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])
#
#
#       # 提交，不然无法保存新建或者修改的数据
#       print(row)
#       conn.commit()
#
#       # 关闭游标
#       cursor.close()
#       # 关闭连接
#       conn.close()





