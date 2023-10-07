import pandas as pd
import json 
import time

import requests

url = "https://twelve-data1.p.rapidapi.com/time_series"


class Portfolio():
    def __init__(self, portfolio_owner):
        self.portfolio_owner = portfolio_owner
        self.portfolios = self.load_portfolios()
        if portfolio_owner in self.portfolios:
            self.stocks = df = pd.DataFrame(self.portfolios[portfolio_owner])
            print('Portfolio loaded.')
        else: 
            self.create_portfolios(self.portfolios,portfolio_owner)

            
    
    def load_portfolios(self):
        f = open('data.json',) 
        # returns JSON object as a dictionary 
        data = json.load(f) 
        return data
    
    def create_portfolios(self,portfolios,owner):
        print('Portfolio not found, a new will be created.')
        time.sleep(2)
        portfolios[owner]=[]
        self.stocks = dict()
        print('Portfolio created. Please use the function to add stocks.')
        with open('data.json', 'w') as f:
            json.dump(portfolios, f)
            f.close()
         
    def add_stock(self, ticker, amount, price, value):
        new_row = {"Ticker": ticker, "Amount": amount, "Price": price, "Value": value}
        self.stocks = pd.concat([self.stocks, pd.DataFrame([new_row])], ignore_index=True)
        self.portfolios[self.portfolio_owner].append(new_row)
        with open('data.json', 'w') as f:
            json.dump(self.portfolios, f)
            f.close()
        return
    
    def update_prices(self, ticker):
        querystring = {"symbol":ticker,"interval":"1day","outputsize":"1","format":"json"}

        headers = {
            "X-RapidAPI-Key": "61d11dfc19msh8f1adb96bd2e05ep1030d1jsn073be1c1af0e",
            "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        dict = response.json()
        
        return float(dict['values'][0]['close'])


    


