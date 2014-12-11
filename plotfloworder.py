import sys
import time
from handledb import *

if __name__ == '__main__':
    date = ''
    if len(sys.argv) < 2: 
        date = time.strftime('%Y-%m-%d', time.localtime())
        print date
    else:
        date = sys.argv[1]
        print date
    symbols = getFlowOrderSymbols(date)
    for symbol in symbols:
        data = getSymbolData(symbol)
        plotStock(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
