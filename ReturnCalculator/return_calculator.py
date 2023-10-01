import pandas as pd
from .params import Params



class ReturnCalculator(Params):
    def __init__(self, period, initial_amaount, monthly_contri):
        Params.__init__(self)  
        self.period = period;
        self.initial_amaount = initial_amaount;
        self.monthly_contri = monthly_contri;

        self.df = pd.DataFrame([[period, initial_amaount, monthly_contri]]
                               ,columns=['Period','InitialAmount','MonthlyContribution']);

        self.return_numbers = self.calculate_return()



    def calculate_return(self):
        x = self.initial_amaount;
        y = [];
        for i in range(self.period*12):
            z = x*((self.params['return']/12)+1);
            y.append(z);
            x = z+self.monthly_contri;
        
        taxed_value = y[-1]-(self.initial_amaount + (self.monthly_contri*(self.period*12-1)));
        if taxed_value < 50000:
            tax = taxed_value*self.params['tax']['lav_aktieskat'];
        else:
            tax = 50000*self.params['tax']['lav_aktieskat']+(taxed_value-50000)*self.params['tax']['high_aktieskat'];
        y[-1] = y[-1]-tax;
        return taxed_value,y

    
