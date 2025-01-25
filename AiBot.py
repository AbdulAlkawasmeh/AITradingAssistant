from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting  # Corrected import
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime 
from alpaca_trade_api import REST 
from pandas import Timedelta
#from finbert_utils import estimate_sentiment


API_KEY = "PKSL0ILTFDT9GT29WHJ2" 
API_SECRET = "nkFy8nkbv2y39xUua3U4MXbuM3FnrbMIHH07jCB5" 
BASE_URL = "https://paper-api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY":API_KEY, 
    "API_SECRET": API_SECRET, 
    "PAPER": True
}


class MLTrader(Strategy): 
    def initialize(self, symbol:str="SPY", cash_at_risk:float=.5): 
        self.symbol = symbol
        self.sleeptime = "24H" 
        self.last_trade = None 
        self.cash_at_risk = cash_at_risk
        self.api = REST(base_url=BASE_URL, key_id=API_KEY, secret_key=API_SECRET)

    def on_trading_iteration(self):
        if self.last_trade==None:
            order=self.create_order(self.symbol,10,"buy",type="market")
            self.submit_order(order)
            self.last_trade="buy"


start_date=datetime(2022,12,10)

end_date=datetime(2024,12,31)

broker=Alpaca(ALPACA_CREDS)
strategy=MLTrader(name='cryptobot', broker=broker, parameters={})

# Correct usage of YahooDataBacktesting
strategy.backtest(YahooDataBacktesting, start_date, end_date, parameters={"symbol":"SPY"})
