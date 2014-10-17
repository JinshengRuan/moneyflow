import sqlite3

def searchStock():
    con = sqlite3.connect('moneyflow.db')
    cur = con.cursor()
    while 1:
        s = raw_input("Please input the stock symbol:\n")
        if s == 'o':
            break
        sql = 'select * from lxjlr where symbol=' + '"' + s + '"'
        cur.execute(sql)
        res = cur.fetchall()
        for stock in res:
            for item in stock:
                print item,
            print
    cur.close()
    con.close()

if __name__ == '__main__':
    searchStock()
