import pandas as pd
import json 
import time





class Portfolio():
    def __init__(self, portfolio_owner):
        portfolios = self.load_portfolios()
        if portfolio_owner in portfolios:
            self.stocks = df = pd.DataFrame(portfolios[portfolio_owner])
            print('Portfolio loaded.')
        else: 
            self.create_portfolios(portfolios,portfolio_owner)

            
    
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
         
    def add_stock(self, ticker, amount):
        new_row = {"ticker": ticker, "amount": amount}
        self.stocks = pd.concat([self.stocks, pd.DataFrame([new_row])], ignore_index=True)
        return


    


