import sqlite3
import sys
import time

def getFlowOrder(date):
    con = sqlite3.connect('moneyflow.db')
    cur = con.cursor()
    dateStr = ' date=' + '"' + date + '" and'
    flowDaysStr = ' flowDays >= 2 and flowDays < 5 and'
    changeStr = ' changeRatio < 0.50 and'
    turnoverStr = ' turnover >= 0.15 and turnover <= 0.9 and'
    netAmountStr = ' netAmount > 0 '
    sql = 'select * from lxjlr where' + dateStr + flowDaysStr + changeStr + turnoverStr + netAmountStr + 'order by changeRatio/netAmount desc limit 50'
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
    
    
    
