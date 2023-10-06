import pandas as pd
from .params import Params



class ReturnCalculator(Params):
    def __init__(self, period, initial_amount, monthly_contri):
        Params.__init__(self)  
        self.period = period;
        self.initial_amount = initial_amount;
        self.monthly_contri = monthly_contri;

        self.df = pd.DataFrame([[period, initial_amount, monthly_contri]]
                               ,columns=['Period','InitialAmount','MonthlyContribution']);

        self.return_numbers = self.calculate_return(self.period, self.initial_amount, self.monthly_contri);



    def calculate_return(self, period, initial_amount, monthly_contri):
        x = initial_amount;
        y = [x];
        for i in range(period*12):
            z = x*((self.params['return']/12)+1);
            x = z+monthly_contri;
            y.append(x);
            
        
        taxed_value = y[-1]-(initial_amount + (monthly_contri*(period*12-1)));
        if taxed_value < 50000:
            tax = taxed_value*self.params['tax']['lav_aktieskat'];
        else:
            tax = 50000*self.params['tax']['lav_aktieskat']+(taxed_value-50000)*self.params['tax']['high_aktieskat'];
        return_post_tax = y[-1]-tax;
        return return_post_tax,y

    
