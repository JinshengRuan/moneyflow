from handledb import *

def main():
    symbols = set([])
    dates = getDatesInDB()
    for date in dates:
        symbols = symbols | set(getFlowOrderSymbols(date))
    for symbol in symbols:
        stock = getSymbolData(symbol)
        plotStock(stock[0], stock[1], stock[2], stock[3], stock[4], stock[5]) 

if __name__ == '__main__':
    main()
#    pylab.show()
