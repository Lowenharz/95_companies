from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from pprint import pprint
import pandas


ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')
data, meta_data = ts.get_monthly(symbol='AVGO')
data['4. close'].plot()
plt.title('Intraday Times Series for the AVGO stock (1 min)')
plt.show()
