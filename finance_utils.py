import yfinance as yf



def getTicker(ticker):
    ticker = yf.Ticker(ticker)

    try:
        _ = ticker.info

        return ticker
    except:
        print(f"Cannot get info of {ticker}, it probably does not exist")
        return None

class TickerProcessor:
    def __init__(self, popularityThreshold, skipWords):
        self.checkedTickers = {}
        self.nonTickers = skipWords
        self.popularityThreshold = popularityThreshold
        

    # ToDo: skip bumping the counter for multiple same post occurence
    def parseTickers(self, text):
        tokenizedText = text.split()
        for token in tokenizedText:
            toCheck = token
            if token[0] == '$':
                toCheck = token[1:]
            if not toCheck.isalpha():
                continue
            toCheck = toCheck.lower()

            if len(toCheck) > 4 or len(toCheck) < 3:
                continue
            
            if toCheck in self.nonTickers:
                continue
            
            if toCheck in self.checkedTickers:
                self.checkedTickers[toCheck] = (self.checkedTickers[toCheck][0], self.checkedTickers[toCheck][1] + 1)
                continue

            print(f"Checking {toCheck}")
            ticker = getTicker(toCheck)

            self.checkedTickers[toCheck] = (ticker, 1)

    def dump(self):
        for ticker in self.checkedTickers:
            print(ticker, self.checkedTickers[ticker][1], self.checkedTickers[ticker][0])
    
    def fetchEnrichedValidTickers(self):
        ret = {}
        for ticker in self.checkedTickers:
            if self.checkedTickers[ticker][1] >= self.popularityThreshold:
                ret[ticker] = self.checkedTickers[ticker][0]
        
        return ret

        



