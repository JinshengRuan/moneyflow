import sys
import time

from handledb import getFlowOrder

if __name__ == '__main__':
    date = ''
    if len(sys.argv) < 2: 
        date = time.strftime('%Y-%m-%d', time.localtime())
        print date
    else:
        date = sys.argv[1]
        print date
    order = getFlowOrder(date)
    for stock in order:
        for item in stock:
            print item, 
        print
    
    
