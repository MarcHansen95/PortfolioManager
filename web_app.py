import streamlit as st
import pandas as pd
from PortfolioOverview.portfolio import Portfolio
import plotly.express as px

st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:300px !important;
}
</style>
""", unsafe_allow_html=True)


st.write("""
# Portfolio Overview
""")




a =  Portfolio('Select a portfolio')
owners = []
for i in a.portfolios:
    owners.append([i][0])



with st.sidebar:
    owner = st.selectbox("Chose Portfolio", owners)


if owner != "Select a portfolio":
    st.header("Stocks of " + owner, anchor=None,divider='rainbow')
    col1, col2 = st.columns((2,1))
    a =  Portfolio(owner) 
    df = pd.DataFrame(a.stocks)
    with col1: 
        st.dataframe(df)


    a = Portfolio(owner)
    
    fig = px.bar(df, x="Ticker", y="Weight", title="Portfolio")
    with col2:
        st.plotly_chart(fig, use_container_width=True)

    



#print('Portfolio chosen')
# print('Adding')
# a.add_stock("FAKE", 10, 10, 100)
# print('Added')

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'San Francisco', 'Los Angeles']
# }

# df = pd.DataFrame(data)
 

# st.line_chart(df)