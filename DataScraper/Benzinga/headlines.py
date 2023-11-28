import pandas as pd
from benzinga import news_data
import datetime
import os.path as path

def headlines_getter(t_start = "2020-01-01"):
    NASDAQ = ["AAPL", "MSFT", "AMZN", "NVDA", "META", "TSLA", "GOOGL", "AVGO", "COST", "INTC"]
    # Define data as a list of dictionaries
    data_to_insert = [
    ]
    t_end = datetime.datetime.today().strftime('%Y-%m-%d')
    start = datetime.datetime.strptime(t_start, "%Y-%m-%d")
    end = datetime.datetime.strptime(t_end, "%Y-%m-%d")
    date_generated = pd.date_range(start, end)
    date_generated = date_generated.date

    api_key = "43eaee64ec7c4ee8b855f2ecd9b728ed"
    paper = news_data.News(api_key)

    for date in date_generated:
        stories = paper.news(date_from= f"{date}", date_to= f"{date}", pagesize=100)
        if len(stories) > 0:
            titles = list(pd.DataFrame(stories)['title'])
            titles = " ".join(titles)
            data_to_insert.append({"Date": date, "Titles": titles})

    df = pd.DataFrame(data_to_insert)
    # print(pd.to_datetime(df['Date']))
    # df = pd.to_datetime(df['Date']).date
    # save_path = path.abspath(path.join(__file__, '../..', 'Benzinga/data/benzinga_headlines.xlsx'))
    # df.to_excel(save_path)
    return df


