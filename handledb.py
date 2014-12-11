#-*- coding: utf-8 -*-
import sqlite3
import pylab
import numpy

def getFlowOrder(date):
    order = []
    con = sqlite3.connect('moneyflow.db')
    cur = con.cursor()
    sql = 'select * from lxjlr where date=' + '"' + date + '" ' + 'order by masterAmount desc limit 50'
    print sql
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    con.close()
    for line in res:
        order.append([item for item in line])
    return order

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
    name = None
    dates = []
    trades = []
    turnovers = []
    amounts = []
    masterAmounts = []
    con = sqlite3.connect('moneyflow.db')
    cur = con.cursor()
    sql = 'select date, name, trade, turnover, amount, masterAmount from lxjlr where symbol=' + '"' + symbol + '"'
    cur.execute(sql)
    res = cur.fetchall()
    cur.close()
    con.close()
    for line in res:
        dates.append(line[0])
        name = line[1]
        trades.append(line[2])
        turnovers.append(line[3])
        amounts.append(line[4])
        masterAmounts.append(line[5])
    return (dates, symbol, name, trades, turnovers, amounts, masterAmounts)

pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']   
pylab.mpl.rcParams['axes.unicode_minus'] = False
def plotStock(dates, symbol, name, trades, turnovers, amounts, masterAmounts):
    masterAmounts = numpy.array(masterAmounts)
    amounts = numpy.array(amounts)
    numpy.seterr(all='ignore')
    masters = (masterAmounts / amounts) * 100
    masters[numpy.isnan(masters)] = 0
    masterAmounts = masterAmounts / 10000000
    turnovers = pylab.array(turnovers)
    turnovers = turnovers * 100
    pylab.figure(figsize=(16,10), dpi=200)
    pylab.subplot(3,1,1)
    pylab.title(symbol +  ' ' + name + ' (' + dates[-1] + ')')  
    pylab.plot(trades, color = 'black', label = u'收盘价格')
    pylab.ylabel(u'价格')
    pylab.legend(loc = 'upper left')
    pylab.autoscale(True, 'both', None)
    pylab.grid(True)
    pylab.subplot(3,1,2)
    pylab.plot(masterAmounts, color = 'red', label = u'主力流入')
    pylab.ylabel(u'千万')
    pylab.legend(loc = 'upper left')
    pylab.autoscale(True, 'both', None)
    pylab.grid(True)
    pylab.subplot(3,1,3)
    pylab.plot(masters, color = 'blue', label = u'主力占比')
#    pylab.plot(turnovers, color = 'green', label = u'换手率')
    pylab.xlabel(u'日期')
    pylab.ylabel(u'百分比-100%')
    pylab.legend(loc = 'upper left')
    pylab.autoscale(True, 'both', None)
    pylab.grid(True)
    pylab.savefig(symbol, dpi=200)
