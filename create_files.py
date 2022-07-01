import os
import csv


def create_csv_if_not_exists():
    path = os.path.dirname(os.path.abspath(__file__))
    sold_csv_path = os.path.join(path, "sold.csv")
    bought_csv_path = os.path.join(path, "bought.csv")
    inventory_csv_path = os.path.join(path, "inventory.csv")
    data_csv_path = os.path.join(path, "data.csv")
    data_csv_path_before_sold = os.path.join(path, "databs.csv")
    if not os.path.exists(sold_csv_path):
        headers_sold = ["id", "bought_id", "sell_date", "sell_price"]
        with open("sold.csv", "w") as sold:
            verkocht = csv.writer(sold)
            verkocht.writerow(headers_sold)
    if not os.path.exists(bought_csv_path):
        headers_bought = [
            "id",
            "product_name",
            "buy_date",
            "buy_price",
            "expiration_date",
        ]
        with open("bought.csv", "w") as bought:
            gekocht = csv.writer(bought)
            gekocht.writerow(headers_bought)
    if not os.path.exists(inventory_csv_path):
        headers_inventory = [
            "bought_id",
            "product_name",
            "count",
            "buy_price",
            "expiration_date",
        ]
        with open("inventory.csv", "w") as inventory:
            inventaris = csv.writer(inventory)
            inventaris.writerow(headers_inventory)
    if not os.path.exists(data_csv_path):
        headers_data = [
            "bought_id",
            "product_name",
            "buy_price",
            "buy_date",
            "expiration_date",
            "sell_id",
            "sell_date",
            "sell_price",
        ]
        with open("data.csv", "w") as data:
            gegevens = csv.writer(data)
            gegevens.writerow(headers_data)
    if not os.path.exists(data_csv_path_before_sold):
        headers_data = [
            "bought_id",
            "product_name",
            "buy_price",
            "buy_date",
            "expiration_date",
        ]
        with open("databs.csv", "w") as data:
            gegevens = csv.writer(data)
            gegevens.writerow(headers_data)
