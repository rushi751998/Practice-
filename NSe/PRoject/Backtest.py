import yfinance as yf
import pandas as pd, copy
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# function for getting all trades data for single stock
def symbol_backtest(symbol):
    
    df = yf.Ticker(f"{symbol}.NS").history(period="5y")

    df["Ma_10"] = round(df["Close"].rolling(window=5).mean(), 2)
    df["Ma_50"] = round(df["Close"].rolling(window=50).mean(), 2)

    # list variable for collecting completed trades in particular symbol
    symbol_trades = []

    trade = {"Symbol": None, "Buy/Sell": None, "Entry Price": None, "Entry Date": None, "Exit Price": None, "Exit Date": None}

    position = None

    for i in df.index[49:]: 

        # this is for exit sell position and enter buy position
        if df["Ma_10"][i] > df["Ma_50"][i] and position != "Buy":
            
            if trade['Symbol'] is not None:
                trade["Exit Price"] = round(df['Close'][i], 2)
                trade["Exit Date"] = i
                # A trade is complected after exit and we append this trade in our list variable
                symbol_trades.append(copy.deepcopy(trade))

            if position is not None:
                
                trade["Symbol"] = symbol
                trade["Buy/Sell"] = "Buy"
                trade["Entry Price"] = round(df['Close'][i], 2)
                trade["Entry Date"] = i

            
            position = "Buy"

            # print(f"{position} : at {round(df['Close'][i],2)} and Date {i}")

        # this is for exit buy position and enter sell position and opposite of buy block
        if df["Ma_10"][i] < df["Ma_50"][i] and position != "Sell":
            if trade['Symbol'] is not None:
                trade["Exit Price"] = round(df['Close'][i], 2)
                trade["Exit Date"] = i
                symbol_trades.append(copy.deepcopy(trade))
            if position is not None:
                trade["Symbol"] = symbol
                trade["Buy/Sell"] = "Sell"
                trade["Entry Price"] = round(df['Close'][i], 2)
                trade["Entry Date"] = i
            position = "Sell"
            # print(f"{position} : at {round(df['Close'][i],2)} and Date {i}")

    return symbol_trades


# define multiple stock list for backtesting
symbol_list = ["Reliance", "Tatamotors", "Tatasteel", "Upl"]

# colling all trades from all stocks and getting at one place for analyse
total_trades = []

# loop on symbol list for backtesting stocks one by one
for symbol in symbol_list:
    # getting return trades
    symbol_trades = symbol_backtest(symbol)
    # loop for append this stocks trades in main variable total_trades
    for trade in symbol_trades:
        total_trades.append(trade)


# for analyse main variable where we collected data
def analyse_data(data):
    # from list to convert data in dataframe for better analysis
    df = pd.DataFrame(data)

    # calculate per trade return
    # divide total capital in len of stocks so that each stock have equal capital invested
    df["Per trade return"] = np.where(df['Buy/Sell'] == "Buy",
                                      round((df["Exit Price"] - df["Entry Price"])*100/df["Entry Price"]/len(symbol_list), 2),
                                      round((df["Entry Price"] - df["Exit Price"])*100/df["Entry Price"]/len(symbol_list),2))
    df = df.sort_values("Exit Date", ascending=True).reset_index(drop=True)

    # calculate probability of strategy
    df['Probability'] = ((np.where(df["Per trade return"] > 0, 1, 0).cumsum())*100/(np.where(df["Per trade return"] != np.NAN, 1, 0).cumsum())).round(2)
    # calculate cumulative return
    df["Return"] = df["Per trade return"].cumsum().round(2)
    # calculate drawdown
    df["Drawdowm"] = df["Return"] - (df["Return"].cummax().apply(lambda x : x if x > 0 else 0))

    # return main dataframe
    return df


a = (analyse_data(total_trades))
print(a)
