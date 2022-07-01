from revenue import Revenue
from tijd import Year_month_day
from datetime import date, datetime, timedelta
import matplotlib.pyplot as plt
from profit import Profit
import numpy as np 
import pandas as pd

def daterange(start_date, end_date):
    end_date=end_date +timedelta(days=1)
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

class start_eind_datum:
    def start_date(start_datum):
        # begin=Year_month_day('2022-06-01')
        begin=Year_month_day(start_datum)
        jaar=int(begin.get_year())
        maand=int(begin.get_month())
        dag=int(begin.get_day())
        start_date= date(jaar, maand, dag)
        return start_date
    def end_date(eind_datum):
        # eind=Year_month_day('2022-06-30')
        eind=Year_month_day(eind_datum)
        jaar=int(eind.get_year())
        maand=int(eind.get_month())
        dag=int(eind.get_day())
        end_date= date(jaar, maand, dag)
        return end_date




#retourneert list van revenue en een list van de datums van de datums tussen start en einde


def revenue_grafic(begin, eind):
    start_date=start_eind_datum.start_date(begin)
    end_date=start_eind_datum.end_date(eind)
    lijst_revenue=[]
    lijst_datums=[]
    for single_date in daterange(start_date, end_date):
        x=Revenue('grafiek', 'date', (single_date.strftime("%Y-%m-%d")))
        lijst_revenue.append(x.run_revenue())
        lijst_datums.append(single_date.strftime("%Y-%m-%d"))
    return lijst_revenue, lijst_datums

def costs_grafic(begin, eind):
    start_date=start_eind_datum.start_date(begin)
    end_date=start_eind_datum.end_date(eind)
    lijst_costs=[]
    lijst_datums=[]
    for single_date in daterange(start_date, end_date):
        x=Profit('grafiek', 'costs', (single_date.strftime("%Y-%m-%d")))
        lijst_costs.append(x.run_profit())
        lijst_datums.append(single_date.strftime("%Y-%m-%d"))
    return lijst_costs, lijst_datums

def profit_grafic(begin, eind):
    start_date=start_eind_datum.start_date(begin)
    end_date=start_eind_datum.end_date(eind)
    lijst_profit=[]
    lijst_datums=[]
    for single_date in daterange(start_date, end_date):
        x=Profit('grafiek', 'profit', (single_date.strftime("%Y-%m-%d")))
        lijst_profit.append(x.run_profit())
        lijst_datums.append(single_date.strftime("%Y-%m-%d"))
    return lijst_profit, lijst_datums

class grafic:
    def __init__(self, data, begin_datum, eind_datum):
        self.data=data
        self.begin_datum=begin_datum
        self.eind_datum=eind_datum 
    
    def revenue(self):
        #print list revenue
        list_revenue=revenue_grafic(self.begin_datum, self.eind_datum)[0]
        #print list datums
        list_data=revenue_grafic(self.begin_datum, self.eind_datum)[1]
        plt.plot(list_data, list_revenue)
        plt.title('Revenue per day')
        plt.ylabel('Revenue in EUR')
        plt.xlabel('Date')
        plt.xticks(fontsize=8, rotation=90)
        plt.show()

    def costs(self):
        #print list revenue
        list_costs=costs_grafic(self.begin_datum, self.eind_datum)[0]
        #print list datums
        list_data=costs_grafic(self.begin_datum, self.eind_datum)[1]
        plt.plot(list_data, list_costs)
        plt.title('Costs per day')
        plt.ylabel('Costs in EUR')
        plt.xlabel('Date')
        plt.xticks(fontsize=8, rotation=90)
        plt.show()
    
    def profit(self):
        #print list revenue
        list_profit=profit_grafic(self.begin_datum, self.eind_datum)[0]
        #print list datums
        list_data=profit_grafic(self.begin_datum, self.eind_datum)[1]
        plt.plot(list_data, list_profit)
        plt.title('Profit per day')
        plt.ylabel('Profit in EUR')
        plt.xlabel('Date')
        plt.xticks(fontsize=8, rotation=90)
        plt.show()
    
    def all_data(self):
        list_revenue=revenue_grafic(self.begin_datum, self.eind_datum)[0]
        list_costs=costs_grafic(self.begin_datum, self.eind_datum)[0]
        list_profit=profit_grafic(self.begin_datum, self.eind_datum)[0]
        list_data=profit_grafic(self.begin_datum, self.eind_datum)[1]
        plt.plot(list_data, list_profit, label='Profit')
        plt.plot(list_data, list_costs, label='Costs')
        plt.plot(list_data, list_revenue, label='Revenue')
        plt.title('Revenue, costs and profit per day')
        plt.ylabel('Data in EUR')
        plt.xlabel('Date')
        plt.xticks(fontsize=8, rotation=90)
        plt.legend()
        plt.show()
    def all_data_csv(self):
        list_revenue=revenue_grafic(self.begin_datum, self.eind_datum)[0]
        list_costs=costs_grafic(self.begin_datum, self.eind_datum)[0]
        list_profit=profit_grafic(self.begin_datum, self.eind_datum)[0]
        list_data=profit_grafic(self.begin_datum, self.eind_datum)[1]
        dict={"Date": list_data, "Revenue": list_revenue, "Costs": list_costs, "Profit": list_profit}
        df=pd.DataFrame(dict)
        naam_csv=f"Financial_data_[{self.begin_datum}]_[{self.eind_datum}].csv"
        df.to_csv(naam_csv, index=False)

    def run_grafic(self):
        if self.data=="revenue":
            self.revenue()
        if self.data=="profit":
            self.profit()
        if self.data=="costs":
            self.costs()
        if self.data=="all_data":
            self.all_data()





class Data_csv:
    def __init__(self, data, begin_datum, eind_datum):
        self.data=data
        self.begin_datum=begin_datum
        self.eind_datum=eind_datum 
    
    def revenue_csv(self):
        list_revenue=revenue_grafic(self.begin_datum, self.eind_datum)[0]
        list_data=revenue_grafic(self.begin_datum, self.eind_datum)[1]
        dict={"Date": list_data, "Revenue": list_revenue}
        df=pd.DataFrame(dict)
        naam_csv=f"Revenue_[{self.begin_datum}]_[{self.eind_datum}].csv"
        df.to_csv(naam_csv, index=False)

    def costs_csv(self):
        list_costs=costs_grafic(self.begin_datum, self.eind_datum)[0]
        list_data=costs_grafic(self.begin_datum, self.eind_datum)[1]
        dict={"Date": list_data, "Costs": list_costs}
        df=pd.DataFrame(dict)
        naam_csv=f"Costs_[{self.begin_datum}]_[{self.eind_datum}].csv"
        df.to_csv(naam_csv, index=False)
    
    def profit_csv(self):
        list_profit=profit_grafic(self.begin_datum, self.eind_datum)[0]
        list_data=profit_grafic(self.begin_datum, self.eind_datum)[1]
        dict={"Date": list_data, "Profit": list_profit}
        df=pd.DataFrame(dict)
        naam_csv=f"Profit_[{self.begin_datum}]_[{self.eind_datum}].csv"
        df.to_csv(naam_csv, index=False)
    

    def all_data_csv(self):
        list_revenue=revenue_grafic(self.begin_datum, self.eind_datum)[0]
        list_costs=costs_grafic(self.begin_datum, self.eind_datum)[0]
        list_profit=profit_grafic(self.begin_datum, self.eind_datum)[0]
        list_data=profit_grafic(self.begin_datum, self.eind_datum)[1]
        dict={"Date": list_data, "Revenue": list_revenue, "Costs": list_costs, "Profit": list_profit}
        df=pd.DataFrame(dict)
        naam_csv=f"Financial_data_[{self.begin_datum}]_[{self.eind_datum}].csv"
        df.to_csv(naam_csv, index=False)

    def run_csv(self):
        if self.data=="revenue":
            self.revenue_csv()
        if self.data=="profit":
            self.profit_csv()
        if self.data=="costs":
            self.costs_csv()
        if self.data=="all_data":
            self.all_data_csv()








