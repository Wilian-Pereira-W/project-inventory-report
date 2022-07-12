import csv
import json
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data_csv(self, product_reader, report_type):
        if report_type == "simples":
            return SimpleReport.generate(product_reader)
        elif report_type == "completo":
            return CompleteReport.generate(product_reader)
        else:
            raise ValueError

    @classmethod
    def import_data_json(self, product, report_type):
        if report_type == "simples":
            return SimpleReport.generate(product)
        elif report_type == "completo":
            return CompleteReport.generate(product)
        else:
            raise ValueError

    @classmethod
    def import_data(self, path, report_type):
        if "csv" in path:
            with open(path, encoding="utf-8") as file:
                product_reader = list(
                    csv.DictReader(file, delimiter=",", quotechar='"')
                )
                return self.import_data_csv(product_reader, report_type)
        elif "json" in path:
            with open(path) as product_file:
                product = json.load(product_file)
                return self.import_data_json(product, report_type)
