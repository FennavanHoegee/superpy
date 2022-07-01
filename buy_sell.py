import pandas as pd
import csv
import re
import os


def date():
    file = open("datum.txt", "r")
    text = file.read()
    pattern = "\d{4}[/-]\d{2}[/-]\d{2}"
    dates = re.findall(pattern, text)
    for date in dates:
        buy_date = date
    return buy_date


def get_bought_id():
    bought_id = 0
    for bought_row in open("bought.csv"):
        bought_id += 1
    return bought_id


class Buy_acties:
    bought_id = get_bought_id()
    datum = date()
    count = 1

    def __init__(self, product_name, buy_price, expiration_date):
        self.product_name = product_name
        self.buy_price = buy_price
        self.expiration_date = expiration_date

    def insert_databs(self):
        with open("databs.csv", "a", newline="") as data_csv:
            writer_data = csv.writer(data_csv)
            rij_data = [
                self.bought_id,
                self.product_name,
                self.buy_price,
                self.datum,
                self.expiration_date,
            ]

            writer_data.writerow(rij_data)
            data_csv.close()

    def insert_bought(self):
        with open("bought.csv", "a", newline="") as bought_csv:
            dictwriter_object = csv.writer(bought_csv)
            rij = [
                self.bought_id,
                self.product_name,
                self.datum,
                self.buy_price,
                self.expiration_date,
            ]
            dictwriter_object.writerow(rij)
            bought_csv.close()

    def insert_inventory(self):

        with open("inventory.csv", "a") as inventory_csv:
            writer_object = csv.writer(inventory_csv)
            with open("inventory.csv", "r") as read_inventory_csv:
                reader_inventory = csv.reader(read_inventory_csv)
                for inventory_row in reader_inventory:
                    if self.product_name in inventory_row:
                        regel_num = reader_inventory.line_num
                        if self.expiration_date == inventory_row[4]:
                            df = pd.read_csv("inventory.csv")
                            df.iloc[(regel_num - 2), 2] += 1
                            df.to_csv("inventory.csv", index=False)
                            exit()

                rij = [
                    self.bought_id,
                    self.product_name,
                    self.count,
                    self.buy_price,
                    self.expiration_date,
                ]
                writer_object.writerow(rij)
                inventory_csv.close()


import pandas as pd
import csv
import re


# ,,,,,,,
# ,,,,,revenue_in_eur
# ,,,profit


class Sell:
    def __init__(self, product_name, sell_price):
        self.product_name = product_name
        self.sell_price = sell_price

    def get_sold_id(self):
        sell_id = 0
        for sold_row in open("sold.csv"):
            sell_id += 1
        return sell_id

    def get_bought_id_sell(self):
        bought_id = 0
        with open("inventory.csv", "r") as inventory:
            reader = csv.reader(inventory)
            for row in reader:
                if self.product_name in row:
                    bought_id = row[0]
        return bought_id

    def get_buy_price(self):
        buy_price = 0
        with open("inventory.csv", "r") as inventory:
            reader = csv.reader(inventory)
            for row in reader:
                if self.product_name in row:
                    buy_price = row[3]
        return buy_price

    def date(self):
        file = open("datum.txt", "r")
        text = file.read()
        pattern = "\d{4}[/-]\d{2}[/-]\d{2}"
        dates = re.findall(pattern, text)
        for date in dates:
            sell_date = date
        return sell_date


class Sell_invoeg(Sell):
    def __init__(self, product_name, sell_price):
        super().__init__(product_name, sell_price)
        self.sold_id = super().get_sold_id()
        self.bought_id = super().get_bought_id_sell()
        self.sell_date = super().date()
        self.buy_price = super().get_buy_price()

    def get_buy_date(self):
        buy_date = 0
        with open("bought.csv", "r") as bought_csv:
            reader = csv.reader(bought_csv)
            for row in reader:
                if self.bought_id in row:
                    buy_date = row[2]
        return buy_date

    def get_expiration_date(self):
        expiration_date = 0
        with open("bought.csv", "r") as bought_csv:
            reader = csv.reader(bought_csv)
            for row in reader:
                if self.bought_id in row:
                    expiration_date = row[4]
        return expiration_date


class Sell_invoeg1(Sell_invoeg, Sell):
    def __init__(self, product_name, sell_price):
        super().__init__(product_name, sell_price)
        self.sold_id = super().get_sold_id()
        self.bought_id = super().get_bought_id_sell()
        self.sell_date = super().date()
        self.buy_price = super().get_buy_price()
        self.buy_date = super().get_buy_date()
        self.expiration_date = super().get_expiration_date()

    def insert_sold(self):
        with open("sold.csv", "a", newline="") as sold_csv:
            dictwriter_object = csv.writer(sold_csv)
            rij_sold = [
                self.sold_id,
                self.bought_id,
                self.sell_date,
                self.sell_price,
            ]
            dictwriter_object.writerow(rij_sold)
            sold_csv.close()

    def inventory_out(self):
        if self.bought_id == 0:
            print("ERROR: Product not in stock.")
            exit()
        df = pd.read_csv("inventory.csv")
        for i, row in df.iterrows():
            if int(row["bought_id"]) == int(self.bought_id):
                if int(row["count"]) > 1:
                    df.loc[i, "count"] -= 1
                    df.to_csv("inventory.csv", index=False)
                else:
                    row_to_deleted = df[(df["bought_id"] == int(self.bought_id))].index[
                        0
                    ]
                    df.drop(df.index[row_to_deleted], axis=0, inplace=True)
                    df.to_csv("inventory.csv", index=False)

    def insert_data(self):
        with open("data.csv", "a") as data_csv:
            writer_data = csv.writer(data_csv)
            rij_data = [
                self.bought_id,
                self.product_name,
                self.buy_price,
                self.buy_date,
                self.expiration_date,
                self.sold_id,
                self.sell_date,
                self.sell_price,
            ]
            writer_data.writerow(rij_data)
            data_csv.close()

    def databs_out(self):
        df = pd.read_csv("databs.csv")
        for i, row in df.iterrows():
            if int(row["bought_id"]) == int(self.bought_id):
                row_to_deleted = df[(df["bought_id"] == int(self.bought_id))].index[0]
                df.drop(df.index[row_to_deleted], axis=0, inplace=True)
                df.to_csv("databs.csv", index=False)
