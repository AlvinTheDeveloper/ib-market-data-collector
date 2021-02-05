import pymysql.cursors
import json

with open('config/keysAndConfig.json') as f:
    keysAndConfig = json.load(f)


class DB:
    def __init__(self, database=None, host=None, port=None,
                 user=None, password=None, returnType='dict'):
        if database:
            self.conn = self.connectDatabase(database, host=host, port=port, user=user, password=password)
            if returnType == 'tuple':
                self.cursor = self.conn.cursor()
            else:
                self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        else:
            self.conn = self.connectDatabase(keysAndConfig['db']['database'],
                                             keysAndConfig['db']['host'],
                                             keysAndConfig['db']['port'],
                                             keysAndConfig['db']['user'],
                                             keysAndConfig['db']['password'])
            if returnType == 'tuple':
                self.cursor = self.conn.cursor()
            elif returnType== 'SSDict':
                self.cursor=self.conn.cursor(pymysql.cursors.SSDictCursor)
            else:
                self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    @staticmethod
    def connectDatabase(database, host, port, user, password):
        return pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=password,
            db=database)

    def createDictCursor(self, database):
        self.conn = self.connectDatabase(database)
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)

    def createTupleCursor(self, database):
        self.conn = self.connectDatabase(database)
        self.cursor = self.conn.cursor()

    def createSSCursor(self, database):
        self.conn = self.connectDatabase(database)
        self.cursor = self.conn.cursor()

    def queryStream(self,sql,data=None,fetchSize=0,cursor=None):
        if cursor is None:
            cursor = self.cursor

        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)


    def query(self, sql, data=None, fetchSize=0, cursor=None):
        # try:
        if cursor is None:
            cursor = self.cursor

        if data:
            cursor.execute(sql, data)
        else:
            cursor.execute(sql)
        if fetchSize == 0:
            return cursor.fetchall()
        elif fetchSize==1:
            return cursor.fetchone()
        elif fetchSize == -1:
            pass
        else:
            return cursor.fetchmany(fetchSize)
        # except TypeError as te:
        #     if not self.cursor:
        #         print("Please create a cursor.")
        #     else:
        #         print(te)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def rollback(self):
        self.conn.rollback()
