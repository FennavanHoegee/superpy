from datetime import datetime, date, timedelta
import re
import os


class Today:
    def makefile_with_date():
        date_object = date.today()
        today = date_object.strftime("%Y-%m-%d")
        current_folder = os.path.dirname(os.path.abspath(__file__))
        datum_csv_path = os.path.join(current_folder, "datum.txt")
        if not os.path.exists(datum_csv_path):
            with open("datum.txt", "w") as f:
                f.write(today)


class Change_date(Today):
    def advance(dagen_to_advance):
        Today.makefile_with_date()
        datum = (datetime.today() - timedelta(days=dagen_to_advance)).strftime(
            "%Y-%m-%d"
        )
        with open("datum.txt", "w") as f:
            f.write(datum)


class Periode:
    def __init__(self, datum):
        self.datum = datum

    def tijdsperiode(self):
        if len(self.datum) == 4:
            """Als user wilt filteren op geheel jaar.
            Voorbeeld input: 2022"""
            input_date_object = datetime.strptime(self.datum, "%Y")
            first_date_object = input_date_object.date().replace(day=1)
            year = first_date_object.strftime("%Y")
            month = 0
        else:
            """als user wilt filteren op bepaalde maanden van een jaar"""
            try:
                """Als user bij input eerst de maand ingeeft, en vervolgens het jaar"
                Voorbeeld input: 7-2022"""
                input_date_object = datetime.strptime(self.datum, "%m-%Y")
                first_date_object = input_date_object.date().replace(day=1)
                year = first_date_object.strftime("%Y")
                month = first_date_object.strftime("%m")
            except:
                """Als user bij input eerst het jaar ingeeft, en vervolgens de maand"
                Voorbeeld input: 2022-7"""
                input_date_object = datetime.strptime(self.datum, "%Y-%m")
                first_date_object = input_date_object.date().replace(day=1)
                year = first_date_object.strftime("%Y")
                month = first_date_object.strftime("%m")
        return year, month
    def tijdsperiode_dag(self):
        input_date_object = datetime.strptime(self.datum, "%Y-%m-%d")

        first_date_object = input_date_object.date()
        year = first_date_object.strftime("%Y")
        month = first_date_object.strftime("%m")
        day=first_date_object.strftime("%d")

        return year, month, day 


class Select_tijd:
    def get_datum_today():
        file = open("datum.txt", "r")
        text = file.read()
        pattern = "\d{4}[/-]\d{2}[/-]\d{2}"
        dates = re.findall(pattern, text)
        for date in dates:
            vandaag = date
        return vandaag

    def get_datum_yesterday():
        file = open("datum.txt", "r")

        text = file.read()
        pattern = "\d{4}[/-]\d{2}[/-]\d{2}"
        dates = re.findall(pattern, text)

        for date in dates:
            vandaag = date
            yesterday = (
                datetime.strptime(vandaag, "%Y-%m-%d").date() - timedelta(days=1)
            ).strftime("%Y-%m-%d")
        return yesterday


class Month_and_year(Periode):
    def get_month(self):
        month = self.tijdsperiode()[1]
        if int(month) > 0:
            return month
        else:
            return None

    def get_year(self):
        year = self.tijdsperiode()[0]
        return year


class Year_month_day(Periode):



    def get_year(self):
        year = self.tijdsperiode_dag()[0]
        return year
    def get_month(self):
        month = self.tijdsperiode_dag()[1]

        return month

    def get_day(self):
        day=self.tijdsperiode_dag()[2]
        return day 

