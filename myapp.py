import pandas as pd
import streamlit as st
import yfinance as yf

st.write(
    """ 
    # Simple Stock price app
    Shown are the stock closing price and volume of Google
    """
)

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d',start='2010-5-31',end='2021-9-30')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)