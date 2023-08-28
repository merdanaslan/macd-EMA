import backtrader as bt
import pandas as pd
from macdcross_ema import MACDCrossoverStrategy


data = pd.read_csv('btc_1h_data_jan_to_aug.csv', parse_dates=True, index_col='timestamp')


data_feed = bt.feeds.PandasData(dataname=data)


cerebro = bt.Cerebro()


cerebro.adddata(data_feed)


cerebro.addstrategy(MACDCrossoverStrategy)

# Set starting cash amount
cerebro.broker.set_cash(10000)

# Set commission
cerebro.broker.setcommission(commission=0.001)


print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())


cerebro.run()


print('Ending Portfolio Value: %.2f' % cerebro.broker.getvalue())

cerebro.plot()
