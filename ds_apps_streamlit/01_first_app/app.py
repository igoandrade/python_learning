import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple stock Price App

Shown are the stock closing price volume of Google!

""")

# define the ticker symbol
tickerSymbol = 'GOOGL'

# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2019-12-31', end='2020-12-31')
# Open High Low Close Volume Dividends Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
