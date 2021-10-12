import math
from Vk import VK
import sqlite3 as sql
from tqdm import tqdm
from DataBase import DataBase

token = input("token : ")
domain = input("domain : ")
name_table = input("Name for the new table: ")
vk = VK()
connection = sql.connect("posts.db")
dbase = DataBase(connection)

if __name__ == "__main__":
    dbase.newTable(name_table)
    postsCount = vk.getCount(domain, token)
    print("Count posts: ", postsCount)
    count = math.ceil(postsCount / 100)
    k = 100

    with tqdm(total=count) as ProgressBar:
        for i in range(0, postsCount, k):
            News = vk.wallGet(domain,token, i)
            l = len(News["response"]["items"])
            if l is None or l < 1:
                input("here")
            for n in range(0, l, 1):
                dbase.addNews(News["response"]["items"][n], name_table)
            ProgressBar.update()