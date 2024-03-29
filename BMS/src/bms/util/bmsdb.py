# -*- coding: utf-8 -*-
import sqlite3


class BMSDBSql():
    """
    simpleToolSql for sqlite3
    简单数据库工具类
    编写这个类主要是为了封装sqlite，继承此类复用方法
    """

    def __init__(self, filename=" bms.db"):
        """
        初始化数据库，默认文件名 ./db/bms.db
        filename：文件名
        """
        self.filename = filename
        self.db = sqlite3.connect(self.filename)
        self.c = self.db.cursor()

    def close(self):
        """
        关闭数据库
        """
        self.c.close()
        self.db.close()

    def execute(self, sql, param=None):
        """
        执行数据库的增、删、改
        sql：sql语句
        param：数据，可以是list或tuple，亦可是None
        retutn：成功返回True
        """
        try:
            if param is None:
                self.c.execute(sql)
            else:
                if type(param) is list:
                    self.c.executemany(sql, param)
                else:
                    self.c.execute(sql, param)
            count = self.db.total_changes
            self.db.commit()
        except Exception as e:
            print(e)
            return False, e
        if count > 0:
            return True
        else:
            return False

    def query(self, sql, param=None):
        """
        查询语句
        sql：sql语句
        param：参数,可为None
        retutn：成功返回True
        """
        if param is None:
            self.c.execute(sql)
        else:
            self.c.execute(sql, param)
        return self.c.fetchall()

    # def set(self,table,field=" * ",where="",isWhere=False):
    #     self.table = table
    #     self.filed = field
    #     if where != "" :
    #         self.where = where
    #         self.isWhere = True
    #     return True


class BMSDB ():
    def __init__(self):
        self.sqlhelper = BMSDBSql('bms.db')
        self.dbinit()
        self.checkAdminUser()

    def dbinit(self):
        self.sqlhelper.execute('''
    CREATE TABLE if not exists users (
    user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_name TEXT ,
    user_number TEXT,
    user_passwd TEXT,
    class TEXT,
    role TEXT
);
    ''')

        self.sqlhelper.execute('''
    CREATE TABLE if not exists books (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    book_name TEXT default '',
    book_SN TEXT default '',
    book_status TEXT default '',
    user_id TEXT default '',
    user_name TEXT default '',
    date TEXT default '',
    comments TEXT default ''
);
    ''')

    def insertFakeData(self):

        self.sqlhelper.execute("insert into users (user_name, user_number, user_passwd, class, role) values (?,?,?,?,?);",
                               [('andy', '20240251', '8888', '202402', '学生'),
                                ('david', '20240252', '8888', '202402', '学生'),
                                   ('admin', '20240252', '8888', '202402', '管理员')])
        res = self.sqlhelper.query("select * from users;")
        print(res)

        self.sqlhelper.execute("insert into books (book_name, book_SN, book_status, user_id,user_name, date, comments) values (?,?,?,?,?,?,?);",
                               [('冰与火之歌', '202402-1', '空闲', '', '', '202220103', 'good'),
                                ('Alice in wonder', '202402-2',
                                 '维护', '', '', '202220104', 'bad'),
                                   ('Robinson', '202402-3', '借出', '1', 'andy', '20220105', 'no comments')])
        res = self.sqlhelper.query("select * from books;")
        print(res)

    def checkUser(self, user, passwd):
        res = self.sqlhelper.query(
            "select * from users where user_name =? and user_passwd = ? ", [user, passwd])
        if (len(res) <= 0):
            return False
        for row in res:
            print(row)
        return True

    def checkAdminUser(self):
        res = self.sqlhelper.query(
            "select * from users where user_name =? ", ['admin'])
        if (len(res) > 0):
            return

        self.sqlhelper.execute("insert into users (user_name, user_number, user_passwd, class, role) values (?,?,?,?,?);",
                               [('admin', '20240252', '8888', '202402', '管理员')])
        res = self.sqlhelper.query("select * from users;")
        return

    def searchBook(self, a_bkstatus, a_bkname, a_bkusername):
        count = False

        sql1 = "select book_name,book_SN, book_status, user_name, user_id, date, comments from books"
        # sql1 = "select * from books"
        if (a_bkname == None):
            a_bkname = ""

        if (a_bkusername == None):
            a_bkusername = ""

        if a_bkstatus != "所有":
            sql1 += ' where book_status="' + a_bkstatus + '"' + " and "
        else:
            sql1 += ' where'

        sql1 += " book_name like '%" + a_bkname + "%'"
        sql1 += " and user_name like '%" + a_bkusername + "%'"

        print(sql1)
        res = self.sqlhelper.query(sql1)
        return res

    def searchBookbySN(self, a_bksn):
        count = False

        sql1 = "select book_name,book_SN, book_status, user_name, user_id, date, comments from books"
        # sql1 = "select * from books"
        sql1 += ' where book_sn="' + a_bksn + '"'

        print(sql1)
        res = self.sqlhelper.query(sql1)
        return res

    def deleteBookbySN(self, a_bksn):
        count = False

        sql1 = "delete from books"
        sql1 += ' where book_sn="' + a_bksn + '"'

        print(sql1)
        res = self.sqlhelper.execute(sql1)
        return res

    def updateBookbySN(self, a_bksn, bookinfo):
        bookinfo.append(a_bksn)
        sql1 = 'update books set book_name="%s", book_SN="%s", book_status="%s",  user_name ="%s", user_id ="%s", date ="%s", comments ="%s" where book_SN="%s";' % (
            tuple(bookinfo))
        print(sql1)
        res = self.sqlhelper.execute(sql1)
        print(res)
        return res

    def addBook(self, a_bkname, a_bksn, a_bkcomments):
        self.sqlhelper.execute("insert into books (book_name, book_SN, book_status, user_id, user_name, date, comments) values (?,?,?,?,?,?,?);",
                               [(a_bkname, a_bksn, '维护', '', '', '', a_bkcomments)])
        res = self.searchBook("所有", a_bkname, "")
        print(res)


if __name__ == "__main__":
    """
    测试代码
    """
    db = BMSDB()
    db.insertFakeData()
    db.checkUser("andy", "8888")
    db.searchBook("借出", "", "")
