import yfinance as yf
import matplotlib.pyplot as plt

def fetch_and_plot(symbol, start_date, end_date):
    tkr = yf.Ticker(symbol)

    info = tkr.info
    name = info['shortName']


    data = tkr.history(start=start_date, end=end_date)
    plt.figure(figsize=(12,6))
    data['Close'].plot(title=f'{name} Stock Closing Prices') 
    plt.xlabel('Date')
    plt.ylabel('Closing Price (in currency)')
    plt.grid(True)
    plt.show()

def get_info(symbol):
    tkr = yf.Ticker(symbol)
    data = tkr.info
    for k in data:
        print(f' {k} Value: {data[k]}')
    

start_date = '2020-01-01'
end_date = '2023-08-12'

symbol = input('enter the stock ticker: ')

#fetch_and_plot(symbol, start_date, end_date)

get_info(symbol)