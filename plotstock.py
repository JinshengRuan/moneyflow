from handledb import *

def main():
    while 1:
        symbol = raw_input("Please input the stock symbol:\n")
        if symbol == 'o':
            break
        data = getSymbolData(symbol)
        plotStock(data[0], data[1], data[2], data[3], data[4], data[5], data[6])

if __name__ == '__main__':
    main()
