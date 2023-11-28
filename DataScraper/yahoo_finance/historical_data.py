import yfinance as yahooFinance
import os.path as path
import pandas as pd

def historicaldata_getter(date, ticker = 'QQQ'):
    NASDAQInformation = yahooFinance.Ticker(ticker)
    # Valid options are 1d, 5d, 1mo, 3mo, 6mo, 1y,
    # 2y, 5y, 10y and ytd.
    # save_path = path.abspath(path.join(__file__, '../..', 'yahoo_finance/data/historical_data.csv'))
    data = NASDAQInformation.history(period="10y")[["Open", "High", "Low", "Close", "Volume"]]
    data = data.loc[date:]
    data["Date"] = pd.to_datetime(data.index).date
    # data = data.reset_index()
    return data.reset_index(drop=True)
