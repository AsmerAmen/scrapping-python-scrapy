import sqlite3
import csv

if __name__ == '__main__':
    conn = sqlite3.connect("amazon.db")
    cur = conn.cursor()

    priceless_products = cur.execute("""SELECT link FROM smart_home_db WHERE price = 0""").fetchall()
    # print(priceless_products)
    # print(type(priceless_products[0]))
    priceless_products = [list(item) for item in priceless_products]
    # print(type(priceless_products[0]))
    print(priceless_products)
    print(len(priceless_products))

    with open('priceless_products', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(priceless_products)

