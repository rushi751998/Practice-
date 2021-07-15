from kiteconnect import KiteConnect


key = "api_key"   # change

kite = KiteConnect(api_key=key)

access_token = "access_token"   # change

kite.set_access_token(access_token=access_token)

# live_data = Get_live_data

symbol = "reliance"
buy_sell = "sell"
quantity = 1

if buy_sell.upper() == "BUY":
    order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                exchange=kite.EXCHANGE_NSE,
                                tradingsymbol=symbol.upper(),
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=quantity,
                                product=kite.PRODUCT_MIS,
                                order_type=kite.ORDER_TYPE_MARKET,
                                validity=kite.VALIDITY_DAY)
    print(order_id)
elif buy_sell.upper() == "SELL":
    order_id = kite.place_order(variety=kite.VARIETY_REGULAR,
                                exchange=kite.EXCHANGE_NSE,
                                tradingsymbol=symbol.upper(),
                                transaction_type=kite.TRANSACTION_TYPE_SELL,
                                quantity=quantity,
                                product=kite.PRODUCT_MIS,
                                order_type=kite.ORDER_TYPE_MARKET,
                                validity=kite.VALIDITY_DAY)
    print(order_id)
else:
    print("No order!!!")
