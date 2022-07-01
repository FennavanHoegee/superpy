
from tijd import Select_tijd
from datetime import datetime
import pandas as pd
from tabulate import tabulate 
import csv 


class Inventory:
    def __init__(self, datum):
        self.datum = datum

    def inventory(self, datum):
        if self.datum == "today":
            datum = Select_tijd.get_datum_today()
            datum = datetime.strptime(datum, "%Y-%m-%d")
            return datum
        if self.datum == "yesterday":
            datum = Select_tijd.get_datum_yesterday()
            datum = datetime.strptime(datum, "%Y-%m-%d")
            return datum

    def inventory_report(self):
        with open('inventory.csv', 'rt') as f:
            csv_reader = csv.reader(f)
            x = []
            for line in csv_reader:
                x += ([line])
            print(tabulate(x, headers='firstrow', tablefmt='fancy_grid'))

