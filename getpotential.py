import sqlite3

def getDatesInDB():
    con = sqlite3.connect('moneyflow.db')
    cur = con.cursor()
    sql = 'SELECT distinct date from lxjlr'
    cur.execute(sql)
    datas = cur.fetchall()
    cur.close()
    con.close()
    dates = []
    for data in datas:
        dates.append(data[0])
    return dates

def getFlowOrderSymbols(date):
    symbols = []
    con = sqlite3.connect('moneyflow.db')
    cur = con.cursor()
    sql = 'select symbol from lxjlr where date=' + '"' + date + '" ' + 'order by masterAmount desc limit 50'
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    con.close()
    for line in res:
        symbols.append(line[0])
    return symbols

def getSymbolData(symbol):
    dates = []
    trades = []
    masterAmounts = []
    con = sqlite3.connect('moneyflow.db')
    cur = con.cursor()
    sql = 'select trade, masterAmount from lxjlr where symbol=' + '"' + symbol + '"'
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    con.close()
    for line in res:
        trades.append(line[0])
        masterAmounts.append(line[1])
    return (symbol, trades, masterAmounts)

import pylab
def plotStock(symbol, trades, masterAmounts):
    masters = pylab.array(masterAmounts)
    masters = masters / 10000000
    pylab.figure()
    pylab.subplot(2,1,1)
    pylab.title(str(symbol))
    pylab.plot(trades, color = 'blue')
    pylab.xlabel('date')
    pylab.ylabel('price')
    pylab.grid(True)
    pylab.subplot(2,1,2)
    pylab.plot(masters, color = 'red', label = 'Amount')
    pylab.xlabel('date')
    pylab.ylabel('money')
    pylab.grid(True)
    pylab.savefig(symbol)

def main():
#    stocks = []
    symbols = set([])
    dates = getDatesInDB()
    for date in dates:
        symbols = symbols | set(getFlowOrderSymbols(date))
    for symbol in symbols:
        stock = getSymbolData(symbol)
        plotStock(stock[0], stock[1], stock[2]) 


if __name__ == '__main__':
    main()
#    pylab.show()
