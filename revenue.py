import pandas as pd
from tijd import Select_tijd, Month_and_year, Year_month_day
from datetime import datetime
from rich.console import Console  
console=Console()



class Revenue:
    df = pd.read_csv("data.csv")

    def __init__(self, report, datum, periode="0"):
        self.report = report
        self.datum = datum
        self.periode = periode

    def revenue_yesterday(self):
        datum = Select_tijd.get_datum_yesterday()
        revenue = self.df.loc[self.df["sell_date"] == datum, "sell_price"].sum()
        return revenue

    def revenue_today(self):
        datum = Select_tijd.get_datum_today()
        revenue = self.df.loc[self.df["sell_date"] == datum, "sell_price"].sum()
        return revenue

    def revenue_tijds_jaar(self, year):
        self.df["sell_date"] = pd.to_datetime(self.df["sell_date"])
        self.df = self.df[self.df["sell_date"].dt.year == int(year)]
        revenue = self.df["sell_price"].sum()
        return revenue

    def revenue_tijds_maand_jaar(self, year, month):
        self.df["sell_date"] = pd.to_datetime(self.df["sell_date"])
        self.df = self.df[self.df["sell_date"].dt.month == int(month)]
        self.df = self.df[self.df["sell_date"].dt.year == int(year)]
        revenue = self.df["sell_price"].sum()
        return revenue
    def revenue_tijds_dag(self, year, month, day):
        self.df["sell_date"] = pd.to_datetime(self.df["sell_date"])
        self.df = self.df[self.df["sell_date"].dt.month == int(month)]
        self.df = self.df[self.df["sell_date"].dt.year == int(year)]
        self.df = self.df[self.df["sell_date"].dt.day == int(day)]
        revenue = self.df["sell_price"].sum()
        return revenue


    def run_revenue(self):
        if self.report == "revenue":
            if self.datum == "today":
                revenue = self.revenue_today()
                console.print("💵 Today's revenue so far:", revenue, style="bold")
            if self.datum == "yesterday":
                revenue = self.revenue_yesterday()
                console.print("💵 Yesterday's revenue:", revenue, style="bold")
            if self.datum == "date":
                tijds_tuple = Month_and_year(self.periode)
                year = tijds_tuple.get_year()
                month = tijds_tuple.get_month()
                if month is None:
                    revenue = self.revenue_tijds_jaar(year)
                    console.print("💵 Revenue from", year + ":", revenue, style="bold")
                else:
                    revenue = self.revenue_tijds_maand_jaar(year, month)
                    datetime_object = datetime.strptime(month, "%m")
                    full_month_name = datetime_object.strftime("%B")
                    console.print("💵 Revenue from", full_month_name, year + ":", revenue, style="bold")
        if self.report=='grafiek':
            tijds_tuple = Year_month_day(self.periode)
            year = tijds_tuple.get_year()
            month = tijds_tuple.get_month()
            day=tijds_tuple.get_day()
            revenue = self.revenue_tijds_dag(year, month, day)
            datetime_object = datetime.strptime(month, "%m")
            full_month_name = datetime_object.strftime("%B")
            return revenue


