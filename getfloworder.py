import sqlite3
import sys
import time

def getFlowOrder(date):
    con = sqlite3.connect('moneyflow.db')
    cur = con.cursor()
    sql = 'select * from lxjlr where date=' + '"' + date + '" ' + 'order by masterAmount desc limit 50'
    print sql
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    con.close()
    for line in res:
        for item in line:
            print item,
        print

if __name__ == '__main__':
    date = ''
    if len(sys.argv) < 2: 
        date = time.strftime('%Y-%m-%d', time.localtime())
        print date
    else:
        date = sys.argv[1]
        print date
    getFlowOrder(date)
    
    
    
