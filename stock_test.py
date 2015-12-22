#!/usr/bin/python
#coding:utf-8
import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas.io.data as web

price = web.get_data_yahoo('QIHU', '2010-01-01')['Adj Close']
price.plot()
plt.show()