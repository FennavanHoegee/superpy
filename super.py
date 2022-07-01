import argparse
import textwrap
from create_files import create_csv_if_not_exists
import tijd as tijd
from tijd import Today
from rich.console import Console
from rich.text import Text
from rich.theme import Theme

console=Console()



def main():
    pass


# parsers:
parser = argparse.ArgumentParser(prog='SuperPy', usage='%(prog)s [options]',
    
    formatter_class=argparse.RawDescriptionHelpFormatter, 
    description=textwrap.dedent('''
        Keep track of your inventory.
        -----------------------------
        - Enter the purchased products.
        - Input the products sold.
        - Get an overview of the supermarket's inventory.

        Produce reports on various kinds of data.
        -----------------------------------------
        - Reporting revenue over specified time periods.
        - Reporting profit over specified time periods.
        - Visual reporting of costs, revenue and profit over specified time periods.
        ''')
)



subparsers = parser.add_subparsers(dest="command")

parser.add_argument(
    "--advance-time", "--advance", "--at",
    type=int,
    help='''Setting and advancing the date that the application perceives as 'today'. 
    Enter the number of days you want to go back in time.'''
)

parser.add_argument('--current-date', action="store_true",help="Printing the date that the application perceives as 'today'.")


# buy parsers
buy = subparsers.add_parser("buy", help="Enter your purchased products. ")
buy.add_argument("--product-name", required=True, help="Enter the product name of the purchased product.")
buy.add_argument("--price", required=True, help="Enter the purchase price of the purchased product.", type=float)
buy.add_argument("--expiration-date", required=True, help="Insert the expiration date as: YYYY-MM-DD")

# sell parsers
sell = subparsers.add_parser("sell", help="Enter the products sold.")
sell.add_argument("--product-name", required=True, help="Enter the product name of the product sold.", action="store")
sell.add_argument("--price", required=True, help="Enter the sales price of the product sold.", type=float)

# report parsers
report = subparsers.add_parser("report", help="Produce reports on various kinds of data.")
report_subparser = report.add_subparsers(dest="parser_report")

inventory = report_subparser.add_parser("inventory", help="Get an overview of the supermarket's inventory on various kinds of data.")
inventory.add_argument("--now", action="store_true", help="Report the current inventory.")
inventory.add_argument("--yesterday", action="store_true", help="Report yesterday's inventory.")
inventory.add_argument("--csv", action="store_true", help="Reporting inventory of specified date in csv format")

revenue = report_subparser.add_parser("revenue", help="Reporting revenue over specified time periods.")
revenue.add_argument("--today", action="store_true", help="Report today's revenue so far.")
revenue.add_argument("--yesterday", action="store_true", help="Reporting yesterday's revenue.")
revenue.add_argument("--date", help="1) You can report revenue based on a whole year, insert the specified year as: YYYY. 2) You can also report revenue based on a specific month in a specific year, insert the date as: YYYY-MM.")

profit = report_subparser.add_parser("profit", help="Reporting profit over specified time periods.")
profit.add_argument("--today", action="store_true", help="Report today's profit so far.")
profit.add_argument("--yesterday", action="store_true", help="Reporting yesterday's profit.")
profit.add_argument("--date", help="1) You can report profit based on a whole year, insert the specified year as: YYYY. 2) You can also report profit based on a specific month in a specific year, insert the date as: YYYY-MM.")


grafic = subparsers.add_parser("graphic", help="Show visual reporting of costs, revenue and profit over specified time periods.")
grafic_subparser = grafic.add_subparsers(dest="parser_grafiek")
revenueg= grafic_subparser.add_parser("revenue", help="Show visual reporting of revenue over specified time periods.")
revenueg.add_argument("--begin-date", help="insert date as: YYYY-MM-DD", required=True)
revenueg.add_argument('--end-date', help="insert date as: YYYY-MM-DD", required=True)
profitg= grafic_subparser.add_parser("profit", help="Show visual reporting of profit over specified time periods.")
profitg.add_argument("--begin-date", help="insert date as: YYYY-MM-DD", required=True)
profitg.add_argument('--end-date', help="insert date as: YYYY-MM-DD", required=True)
costsg= grafic_subparser.add_parser("costs", help="Show visual reporting of costs over specified time periods.")
costsg.add_argument("--begin-date", help="insert date as: YYYY-MM-DD", required=True)
costsg.add_argument('--end-date', help="insert date as: YYYY-MM-DD", required=True)
all_datag= grafic_subparser.add_parser("all_data", help="Show visual reporting of costs, revenue and profit over specified time periods.")
all_datag.add_argument("--begin-date", help="insert date as: YYYY-MM-DD", required=True)
all_datag.add_argument('--end-date', help="insert date as: YYYY-MM-DD", required=True)


csv_data = subparsers.add_parser("csv", help="Import financial data into csv format. For example; costs, revenue and profit over specified time periods.")
csv_data_parser = csv_data.add_subparsers(dest="parser_csv")
revenuec= csv_data_parser.add_parser("revenue", help="Show reporting of revenue over specified time periods in csv format.")
revenuec.add_argument("--begin-date", help="insert date as: YYYY-MM-DD", required=True)
revenuec.add_argument('--end-date', help="insert date as: YYYY-MM-DD", required=True)
profitc= csv_data_parser.add_parser("profit", help="Show reporting of profit over specified time periods in csv format.")
profitc.add_argument("--begin-date", help="insert date as: YYYY-MM-DD", required=True)
profitc.add_argument('--end-date', help="insert date as: YYYY-MM-DD", required=True)
costsc = csv_data_parser.add_parser("costs", help="Show reporting of costs over specified time periods in csv format.")
costsc.add_argument("--begin-date", help="insert date as: YYYY-MM-DD", required=True)
costsc.add_argument('--end-date', help="insert date as: YYYY-MM-DD", required=True)
all_datac = csv_data_parser.add_parser("all_data", help="Show reporting of costs, revenue and profit over specified time periods in csv format.")
all_datac.add_argument("--begin-date", help="insert date as: YYYY-MM-DD", required=True)
all_datac.add_argument('--end-date', help="insert date as: YYYY-MM-DD", required=True)





args = parser.parse_args()


if __name__ == "__main__":
    main()
    create_csv_if_not_exists()
    Today.makefile_with_date()


if args.advance_time:
    dagen = args.advance_time
    tijd.Change_date.advance(dagen)
    a = tijd.Select_tijd.get_datum_today()
    print("Ok, datum vervroegd naar:", a, "📆🔙")

if args.current_date:
    a = tijd.Select_tijd.get_datum_today()
    print("De huidige datum die als 'vandaag' wordt beschouwd is:", a, "📆")


from buy_sell import Buy_acties, Sell_invoeg1

if args.command == "buy":
    product_name = args.product_name
    price = args.price
    expiration_date = args.expiration_date
    invoegen = Buy_acties(product_name, price, expiration_date)
    invoegen.insert_databs()
    invoegen.insert_bought()
    invoegen.insert_inventory()
    console.print("OK, inserted! :thumbs_up: ")




if args.command == "sell":
    product_name = args.product_name
    price = args.price
    verkocht = Sell_invoeg1(product_name, price)
    verkocht.inventory_out()
    verkocht.insert_sold()
    verkocht.insert_data()
    verkocht.databs_out()
    console.print("OK, inserted! :thumbs_up: ")

from inventory import Inventory
from revenue import Revenue
from profit import Profit

if args.command == "report":
    if args.parser_report == "inventory":
        if args.now:
            x=Inventory("today")
            x.inventory_report()
        if args.yesterday:
            tijd.Change_date.advance(1)
            x=Inventory("yesterday")
            x.inventory_report()
            Today.makefile_with_date()





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


from data_for_grafic import grafic, profit_grafic
if args.command == "graphic":
    begin_datum= args.begin_date
    eind_datum=args.end_date
    if args.parser_grafiek == 'costs':
        x=grafic('costs', begin_datum, eind_datum)
    if args.parser_grafiek == 'revenue':
        x=grafic('revenue', begin_datum, eind_datum)
    if args.parser_grafiek=='profit':
        x=grafic('profit', begin_datum, eind_datum)
    if args.parser_grafiek=='all_data':
        x=grafic('all_data', begin_datum, eind_datum)
    x.run_grafic()

from data_for_grafic import Data_csv
if args.command == "csv":
    begin_datum= args.begin_date
    eind_datum=args.end_date
    if args.parser_csv == 'costs':
        x=Data_csv('costs', begin_datum, eind_datum)
    if args.parser_csv == 'revenue':
        x=Data_csv('revenue', begin_datum, eind_datum)
    if args.parser_csv=='profit':
        x=Data_csv('profit', begin_datum, eind_datum)
    if args.parser_csv =='all_data':
        x=Data_csv('all_data', begin_datum, eind_datum)
    x.run_csv()


