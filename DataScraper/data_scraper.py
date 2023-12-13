import pandas as pd
from os import path
from Benzinga.headlines import headlines_getter
from Yahoo_finance.historical_data import historicaldata_getter

headlines = headlines_getter(t_start="2016-01-01")
prices = historicaldata_getter(date="2016-01-01")

headlines = headlines[headlines['Date'].isin(prices['Date'])]

merge_df = headlines.merge(prices, on='Date', how='right')
merge_df.fillna("...", inplace=True)

merge_df.set_index = merge_df["Date"]

save_path = path.abspath(path.join(__file__, '../..', 'Feature_engineer/data/data_scrape.xlsx'))
merge_df.to_excel(save_path, index=False)
