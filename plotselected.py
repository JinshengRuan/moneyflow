from handledb import *

def main():
    symbols = [u'sh600010', u'sh600109', u'sh600255', u'sh600361', u'sh600389', u'sh600743', u'sh600757', u'sh600791', u'sh601989', u'sz000030', u'sz000056', u'sz000059', u'sz000518', u'sz000536', u'sz000561', u'sz000587', u'sz000637', u'sz000682', u'sz000712', u'sz000809', u'sz002149', u'sz002232', u'sz002275', u'sz002288', u'sz002388', u'sz002412', u'sz002420', u'sz002478', u'sz002489', u'sz002557', u'sz002697', u'sz300142', u'sz300196', u'sz300349', u'sz300085', u'sz002472']
    for symbol in symbols:
        data = getSymbolData(symbol)
        plotStock(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

if __name__ == '__main__':
    main()
