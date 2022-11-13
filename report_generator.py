# 1.
# top post [1-3]
# popularity
# price increase/decrease past 24h



def genReport(tickerDict):
    text = "Today's most dicussed tickers on reddit:\n\n"
    for ticker in tickerDict:
        text += ticker
        text += "\n"
    
    text += "\n\n\nLotta love from your devoted butler,\n"
    text += "Meadows"

    return text