import sqlite3 as sql
from datetime import datetime

class DataBase:

    def __init__(self, db):
        self.__db__ = db
        self.__current__ = db.cursor()

    def newTable(self, name_table):
        str1 = "CREATE TABLE IF NOT EXISTS "
        str2 = "(text_post TEXT, data_post INTEGER, id_post INTEGER, c_com INTEGER, c_like INTEGER, c_repost INTEGER, c_view INTEGER)"
        total = str1 + name_table + str2
        self.__current__.execute(total)
        self.__db__.commit()

    def addNews(self, response, name_table) -> bool:
        try:
            self.__current__.execute(f"INSERT INTO {name_table} VALUES(?, ?, ?, ?, ?, ?, ?)",
                                     (response["text"], datetime.utcfromtimestamp(int(response["date"] + (60 * 60 * 3)))
                                      .strftime('%Y-%m-%d %H:%M:%S'), response["id"], response["comments"]["count"],
                                      response["likes"]["count"], response["reposts"]["count"],
                                      response["views"]["count"]))
            self.__db__.commit()
        except sql.Error as e:
            print("Error" + str(e))
            return False
        return True