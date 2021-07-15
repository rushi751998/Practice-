import yfinance as yf
import pandas as pd, copy
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# function for getting all trades data for single stock
def symbol_backtest(symbol):
    """Get single stock historical data and this must be in dataframe format.
    yahoo already provide data in dataframe"""
    df = yf.Ticker(f"{symbol}.NS").history(period="2y")

    """Our strategy is 10 or 50 day moving average crossover.
    applying indicator on dataframe the calculation of moving avg is simple so i don't use any tool.
    you can use ta-lib library for other indicators"""
    df["Ma_10"] = round(df["Close"].rolling(window=10).mean(), 2)
    df["Ma_50"] = round(df["Close"].rolling(window=50).mean(), 2)

    # list variable for collecting completed trades in particular symbol
    symbol_trades = []

    """ dict variable for store current running single trade info that we want, initially there is No trade.
    our trades are in both direction not for buying"""
    trade = {"Symbol": None, "Buy/Sell": None, "Entry Price": None, "Entry Date": None, "Exit Price": None, "Exit Date": None}

    """variable to avoid multiple signal for 1 trade.
    racking previous candle direction or signal (buy/sell) initially there is No direction"""
    position = None

    """  loop for going through 1 by 1 candle forward in time from history .
         checking signal for every candle and note down the trade info when new signal occur.
         start after first 50 candle because there is no 50 day moving avg data"""
    for i in df.index[49:]:
        """checking 10 and 50 moving avg crossover for that particular candle.
        checking there is no same signal as in previous candle """

        """for 1st candle we only want position variable not trade info because we don't have direction .
        if we define ' position == "Sell" ' at the place of ' position != "Buy" ' both are correct but 
        ' position == "Sell" ' not valid for None because initial time our " position == None" 
        we never enter in any block if we do that"""

        # this is for exit sell position and enter buy position
        if df["Ma_10"][i] > df["Ma_50"][i] and position != "Buy":
            """first we exit the opposite position if there is, and store data at exit signal time for that candle.
            if only want exit info if there is sell position,not if there is none initial time as we define"""
            if trade['Symbol'] is not None:
                trade["Exit Price"] = round(df['Close'][i], 2)
                trade["Exit Date"] = i
                # A trade is complected after exit and we append this trade in our list variable
                symbol_trades.append(copy.deepcopy(trade))

            """this "if" for initial time,first signal is not valid,so we don't want data for that.
            because it occured before in time but we got it when we start checking.
            first signal could occur in sell block than we go for that after first signel this if always true.
            Also entry for new position after exit and collect trade info at entry"""

            if position is not None:
                """getting data that we require from that particular signal candle.
                this would also replace previous trade data """
                trade["Symbol"] = symbol
                trade["Buy/Sell"] = "Buy"
                trade["Entry Price"] = round(df['Close'][i], 2)
                trade["Entry Date"] = i

            """ setting variable for that we don't want next signal same 
            if it is same we don't enter in this block " position != "Buy" " """
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

    """getting list variable in return so that we add these trades in main variable when we 
    are doing this for multiple stocks"""
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
a.to_csv("123.csv",index =  False)
