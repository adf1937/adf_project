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


if __name__ == "__main__":
    """
    测试代码
    """
    sql = BMSDBSql()

    f = sql.execute('''
    CREATE TABLE if not exists users (
    user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    user_name TEXT,
    user_number INTEGER,
    user_passwd TEXT,
    class TEXT,
    role INTEGER
);
    ''')

    sql.execute("insert into users (user_name, user_number, user_passwd, class, role) values (?,?,?,?,?);",
                [('andy', 20240251, '8888', '202402', 2),
                 ('david', 20240252, '8888', '202402', 1),
                 ('admin', 20240252, '8888', '202402', 0)])
    res = sql.query("select * from users;")
    print(res)

    f = sql.execute('''
    CREATE TABLE if not exists books (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    book_name TEXT,
    book_SN TEXT,
    status INTEGER,
    user_id INTEGER,
    user_name TEXT,
    date TEXT,
    comments TEXT
);
    ''')

    sql.execute("insert into books (book_name, book_SN, status, user_id,user_name, date, comments) values (?,?,?,?,?,?,?);",
                [('冰与火之歌', '202402-1', 0, 0, '', '202220103', 'good'),
                 ('Alice in wonder', '202402-2', 0, 0, '', '202220104', 'bad'),
                 ('Robinson', '202402-3', 1, 1, 'andy', '20220105', 'no comments')])
    res = sql.query("select * from books;")
    print(res)

    sql.close()
