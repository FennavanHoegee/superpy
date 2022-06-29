import argparse
from create_files.create_files import create_csv_if_not_exists
import tijd.tijd as tijd


def main():
    pass


# parsers:
parser = argparse.ArgumentParser(
    description="Hou uw inventaris bij.",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
subparsers = parser.add_subparsers(dest="command")

parser.add_argument(
    "--advance-time",
    type=int,
    help="voer het aantal dagen in dat u terug wilt gaan in de tijd",
)


# buy parsers
buy = subparsers.add_parser("buy", help="voer gekochte producten in")
buy.add_argument("--product-name", required=True, help="voer product naam in")
buy.add_argument("--price", required=True, help="vul prijs in", type=float)
buy.add_argument("--expiration-date", required=True, help="insert date as: YYYY-MM-DD")

# sell parsers
sell = subparsers.add_parser("sell", help="voer gekochte producten in")
sell.add_argument(
    "--product-name", required=True, help="voer product naam in", action="store"
)
sell.add_argument("--price", help="vul prijs in", type=float)

# report parsers
report = subparsers.add_parser("report", help="report inventory")
report_subparser = report.add_subparsers(dest="parser_report")

inventory = report_subparser.add_parser("inventory")
inventory.add_argument("--now", action="store_true")
inventory.add_argument("--yesterday", action="store_true")

revenue = report_subparser.add_parser("revenue")
revenue.add_argument("--today", action="store_true")
revenue.add_argument("--yesterday", action="store_true")
revenue.add_argument("--date")

profit = report_subparser.add_parser("profit")
profit.add_argument("--today", action="store_true")
profit.add_argument("--yesterday", action="store_true")
profit.add_argument("--date")

args = parser.parse_args()


if __name__ == "__main__":
    main()
    create_csv_if_not_exists()
    tijd.Today.makefile_with_date()


if args.advance_time:
    dagen = args.advance_time
    tijd.Change_date.advance(dagen)
    a = tijd.Select_tijd.get_datum_today()
    print("Ok, datum vervroegd naar:", a)


from buy_and_sell.buy_sell import Buy_acties
from buy_and_sell.buy_sell import Sell_invoeg1

# python super.py buy --product-name orange --price 1.8 --expiration-date 2020-01-01
# python super.py buy --product-name kiwi --price 3.0 --expiration-date 2020-01-01

# python super.py sell --product-name orange --price 3.8
# --expiration-date 2020-01-01
# python super.py sell --product-name kiwi --price 5.0
# --expiration-date 2020-01-01
if args.command == "buy":
    product_name = args.product_name
    price = args.price
    expiration_date = args.expiration_date
    invoegen = Buy_acties(product_name, price, expiration_date)
    invoegen.insert_databs()
    invoegen.insert_bought()
    invoegen.insert_inventory()
    print("OK")


if args.command == "sell":
    product_name = args.product_name
    price = args.price
    verkocht = Sell_invoeg1(product_name, price)
    verkocht.inventory_out()
    verkocht.insert_sold()
    verkocht.insert_data()
    verkocht.databs_out()
    print("OK")

from inventory import inventory_report
from revenue import Revenue
from profit import Profit

if args.command == "report":
    if args.parser_report == "inventory":
        if args.now:
            inventory_report("today")
        if args.yesterday:
            inventory_report("yesterday")

    if args.parser_report == "revenue":
        if args.today:
            revenue = Revenue("revenue", "today")
        if args.yesterday:
            revenue = Revenue("revenue", "yesterday")
        if args.date:
            revenue = Revenue("revenue", "date", args.date)

        revenue.run_revenue()

    if args.parser_report == "profit":
        if args.today:
            profit = Profit("profit", "today")
        if args.yesterday:
            profit = Profit("profit", "yesterday")
        if args.date:
            profit = Profit("profit", "date", args.date)

        profit.run_profit()
