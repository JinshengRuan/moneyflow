from handledb import *
import numpy

def main():
    potentials = []
    symbols = getSymbolsInDB()
    for symbol in symbols:
        dates, sym, name, trades, turnovers, amounts, masterAmounts = getSymbolData(symbol)
        numAmounts = numpy.array(amounts)
        numMasterAmounts = numpy.array(masterAmounts)
        numpy.seterr(all='ignore')
        masters = numMasterAmounts / numAmounts
        masters[numpy.isnan(masters)] = 0
        if len(trades) < 2:
            continue
        if trades[-2] == 0 or trades[-1] == 0:
            continue
        if ((trades[-1] - trades[-2]) / trades[-2] > 0.09)  and (masters[-1] >= 0.15):
            potentials.append(symbol)
            plotStock(dates, sym ,name, trades, turnovers, amounts, masterAmounts)
    print len(potentials)
    print potentials

if __name__ == '__main__':
    main()
