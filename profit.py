from click import style
import revenue
import pandas as pd
from tijd import Select_tijd, Month_and_year, Year_month_day
from datetime import datetime
from rich.console import Console  
from rich.theme import Theme

custom_theme=Theme({"profit":"green", "loss": "bold red"})
console=Console(theme=custom_theme)





class Profit(revenue.Revenue ):
    df = pd.read_csv("data.csv")

    def __init__(self, report, datum, periode="0"):
        super().__init__(report, datum, periode)
        self.revenue_today = super().revenue_today()
        self.revenue_yesterday = super().revenue_yesterday()

    def profit_yesterday(self):
        datum = Select_tijd.get_datum_yesterday()
        self.df = self.df[self.df["sell_date"] == str(datum)]
        buys = self.df["buy_price"].sum()
        profit = self.revenue_yesterday - buys
        profit = round(profit, 2)
        return profit

    def profit_today(self):
        datum = Select_tijd.get_datum_today()
        self.df = self.df[self.df["sell_date"] == str(datum)]
        buys = self.df["buy_price"].sum()
        profit = self.revenue_today - buys
        profit = round(profit, 2)
        return profit

    def profit_tijds_jaar(self, year):
        self.df["sell_date"] = pd.to_datetime(self.df["sell_date"])
        self.df = self.df[self.df["sell_date"].dt.year == int(year)]
        buys = self.df["buy_price"].sum()
        revenue = self.revenue_tijds_jaar(year)
        profit = round(revenue - buys, 2)
        return profit

    def profit_tijds_maand_jaar(self, year, month):
        self.df["sell_date"] = pd.to_datetime(self.df["sell_date"])
        self.df = self.df[self.df["sell_date"].dt.month == int(month)]
        self.df = self.df[self.df["sell_date"].dt.year == int(year)]
        buys = self.df["buy_price"].sum()
        revenue = self.revenue_tijds_maand_jaar(year, month)
        profit = round(revenue - buys, 2)
        return profit
    
    def profit_tijds_dag(self, year, month, day):
        self.df["sell_date"] = pd.to_datetime(self.df["sell_date"])
        self.df = self.df[self.df["sell_date"].dt.month == int(month)]
        self.df = self.df[self.df["sell_date"].dt.year == int(year)]
        self.df = self.df[self.df["sell_date"].dt.day == int(day)]
        buys = self.df["buy_price"].sum()
        revenue = self.revenue_tijds_dag(year, month, day)
        profit = round(revenue - buys, 2)
        return profit
    def costs_tijds_dag(self, year, month, day):
        self.df["sell_date"] = pd.to_datetime(self.df["sell_date"])
        self.df = self.df[self.df["sell_date"].dt.month == int(month)]
        self.df = self.df[self.df["sell_date"].dt.year == int(year)]
        self.df = self.df[self.df["sell_date"].dt.day == int(day)]
        buys = self.df["buy_price"].sum()
        buys = round(buys, 2)
        return buys

    def run_profit(self):
        if self.report == "profit":
            if self.datum == "today":
                profit = self.profit_today()
                if profit <0:
                    console.print("📉 Today's profit so far:", profit, style="loss")
                if profit >=0:
                    console.print("📈 Today's profit so far:", profit, style="profit")
            if self.datum == "yesterday":
                profit = self.profit_yesterday()
                if profit <0:
                    console.print("📉 Yesterday's profit:", profit, style="loss")
                if profit >=0:
                    console.print("📈 Yesterday's profit:", profit, style="profit")
            if self.datum == "date":
                tijds_tuple = Month_and_year(self.periode)
                year = tijds_tuple.get_year()
                month = tijds_tuple.get_month()
                if month is None:
                    profit = self.profit_tijds_jaar(year)
                    if profit < 0:
                        console.print("📉 Profit from", year + ":", profit, style="loss")
                    if profit >= 0:
                        console.print("📈 Profit from", year + ":", profit, style="profit")
                else:
                    profit = self.profit_tijds_maand_jaar(year, month)
                    datetime_object = datetime.strptime(month, "%m")
                    full_month_name = datetime_object.strftime("%B")
                    if profit < 0:
                        console.print("📉 Profit from", full_month_name, year + ":", profit, style="loss")
                    if profit >= 0:
                        console.print("📈 Profit from", full_month_name, year + ":", profit, style="profit")
        if self.report=='grafiek':
            if self.datum=='profit':
                tijds_tuple=Year_month_day(self.periode)
                year=tijds_tuple.get_year()
                month=tijds_tuple.get_month()
                day=tijds_tuple.get_day()
                profit=self.profit_tijds_dag(year, month, day)
                return profit
            if self.datum=='costs':
                tijds_tuple=Year_month_day(self.periode)
                year=tijds_tuple.get_year()
                month=tijds_tuple.get_month()
                day=tijds_tuple.get_day()
                costs=self.costs_tijds_dag(year, month, day)
                return costs

