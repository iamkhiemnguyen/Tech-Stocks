import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Stock Price of Major Tech Companies

## Apple Inc
Shown are the stock closing price and volume of Apple!

""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'id', start= '2010-1-01', end= '2100-12-31')

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
## TESLA
Shown are the stock closing price and volume of Tesla!

""")

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'id', start= '2010-1-01', end= '2100-12-31')

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
## Amazon
Shown are the stock closing price and volume of Amazon!

""")

tickerSymbol = 'AMZN'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'id', start= '2010-1-01', end= '2100-12-31')

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
## Google
Shown are the stock closing price and volume of Google!

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'id', start= '2010-1-01', end= '2100-12-31')

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
## Netflix
Shown are the stock closing price and volume of Netflix!

""")

tickerSymbol = 'NFLX'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'id', start= '2010-1-01', end= '2100-12-31')

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
## Meta
Shown are the stock closing price and volume of Meta!

""")

tickerSymbol = 'META'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'id', start= '2010-1-01', end= '2100-12-31')

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
## Microsoft
Shown are the stock closing price and volume of Microsoft!

""")

tickerSymbol = 'MSFT'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'id', start= '2010-1-01', end= '2100-12-31')

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)

st.write("""
## IBM
Shown are the stock closing price and volume of IBM!

""")

tickerSymbol = 'IBM'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = 'id', start= '2010-1-01', end= '2100-12-31')

st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
### Volume Price
""")
st.line_chart(tickerDf.Volume)