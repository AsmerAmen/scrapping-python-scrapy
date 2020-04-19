# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# Databases:
# import sqlite3
# import mysql.connector
import pymongo

class SpyderUnoPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        # SQLite3
        # self.conn = sqlite3.connect("myquotes.db")
        # self.cur = self.conn.cursor()

        # MySQL
        # self.conn = mysql.connector.connect(
        #     host='localhost',
        #     user='root',
        #     passwd='P@$$w0rd',
        #     database='quotes'
        # )
        # self.cur = self.conn.cursor()

        # MongoDB
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )

    def create_table(self):
        # SQLite3 & MySQL
        # self.cur.execute("""DROP TABLE IF EXISTS quotes_tb""")
        # self.cur.execute("""CREATE TABLE quotes_tb(
        #                     title text,
        #                     author text,
        #                     tag text
        #                     )"""
        #                  )

        # MongoDB
        db = self.conn['quotes']            # Created Database
        self.collection = db['quotes_tb']   # Created Table

    def store_db(self, item):
        # SQLite3
        # self.cur.execute("""INSERT INTO quotes_tb
        #                     VALUES (?,?,?)""", (item['title'][0],
        #                                         item['author'][0],
        #                                         item['tag'][0])
        #                  )
        # self.conn.commit()

        # MySQL
        # self.cur.execute("""INSERT INTO quotes_tb
        #                             VALUES (%s,%s,%s)""", (item['title'][0].strip("“"),
        #                                                    item['author'][0],
        #                                                    item['tag'][0])
        #                  )
        # self.conn.commit()

        # MongoDB
        self.collection.insert(dict(item))

    def process_item(self, item, spider):
        self.store_db(item)
        print("Pipeline: ", item['title'][0])
        return item
