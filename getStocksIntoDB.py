import urllib2
import json
import re
import csv
import time
import sqlite3

def getDate():
    url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssi_get_extend?id=2'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    content = response.read()
    m = re.search(r'[1-9]\d+', content)
    seconds = int(m.group(0))
    date = time.localtime(seconds)
    timeStr = time.strftime('%Y-%m-%d', date)
    return timeStr

def getNumberOfStock():
    url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssc_bkzj_lxjlr?bankuai='
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    content = response.read()
    m = re.search(r'[1-9]\d+', content)
    number = m.group(0)
    return number

def addDoubleQuote(match):
    value = match.group(1)
    return '"' + value + '"' + ':'

def getJsonOfStocks():
    number = getNumberOfStock()
    url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/MoneyFlow.ssl_bkzj_lxjlr?num=' + number + '&sort=cnt_r0x_ratio&asc=0&bankuai='
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    dataJsonStr = response.read()
    dataJsonStrUni = dataJsonStr.decode("GB2312")
    result = re.sub(u'(\w+)\:', addDoubleQuote, dataJsonStrUni)
    stocks = json.loads(result)
    return stocks

def createDB():
    con = sqlite3.connect('moneyflow.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE lxjlr(date TEXT, symbol TEXT, name TEXT, flowDays INTEGER, trade REAL, changeRatio REAL, turnover REAL, amount REAL, netAmount REAL, ratioAmount REAL, masterAmount REAL)')
    cur.close()
    con.close()

def insertData(date, jsonObjs):
    con = sqlite3.connect('moneyflow.db')
    cur = con.cursor()
    for stock in jsonObjs:
        date = date
        symbol = stock[u'symbol']
        name = stock[u'name']
        days = int(stock[u'cnt_r0x_ratio'])
        trade = round(float(stock[u'trade']), 2)
        changeRatio = round(float(stock[u'changeratio']), 3)
        turnover = round(float(stock[u'turnover'])/10000, 4)
        amount = round(float(stock[u'amount']), 2)
        netAmount = round(float(stock[u'netamount']), 2)
        ratioAmount = round(float(stock[u'ratioamount']), 3)
        masterAmount = round(float(stock[u'r0_net']), 2)
        sql = 'INSERT INTO lxjlr VALUES(' + '"' + date + '", ' + '"' + symbol + '", ' + '"' + name + '", ' + str(days) + ', ' + str(trade) + ', ' + str(changeRatio) + ', ' + str(turnover) + ', ' + str(amount) + ', ' + str(netAmount) + ', ' + str(ratioAmount) + ', ' + str(masterAmount) + ')'
        cur.execute(sql)
    con.commit()
    cur.close()
    con.close()

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
    
def main():
    date = getDate()
    dates = getDatesInDB()
    print dates
    if date in dates:
        print 'exist'
    else:
        jsonObjs = getJsonOfStocks()
        insertData(date, jsonObjs)

if __name__ == '__main__':
    main()
