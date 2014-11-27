import sqlite3

def getSymbolData(symbol):
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
    while 1:
        symbol = raw_input("Please input the stock symbol:\n")
        if symbol == 'o':
            break
        data = getSymbolData(symbol)
        plotStock(data[0], data[1], data[2])

if __name__ == '__main__':
    main()
