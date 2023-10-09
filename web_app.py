import streamlit as st
import pandas as pd
from PortfolioOverview.portfolio import Portfolio





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
    st.header("Stocks of " + owner, anchor=None)

    a =  Portfolio(owner) 
    df = pd.DataFrame(a.stocks)
    st.dataframe(df)




    a = Portfolio(owner)
    
    st.bar_chart(data=a.stocks["Weight"], x = ["Hej", "dsd", "sd"], y=None, width=0, height=0, use_container_width=True)


    



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