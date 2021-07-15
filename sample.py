from jarvis import speak
from nsetools import Nse
from pprint  import pprint 
nse = Nse ()

import datetime as dt
import yfinance as yf
time = dt.datetime.now()
Hour = int((time.strftime("%I")).strip("0"))
Minut =int(time.strftime("%M").strip("0"))

a = ["Tata moters","IGL","RELIANCE","SBIN"]



for i in a :
    speak (f"Sir. {i} key  order {Hour} Bajkay. {Minut} Minut pay  place key gaihai. ")
    Minut += 5
    Hour -= 1

speak ("Sir Pleace Check once again")
speak ("Thanks Budy, Have a nice day") 