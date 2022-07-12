import csv
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def import_data(self, path, report_type):
        if "csv" in path:
            with open(path, encoding="utf-8") as file:
                product_reader = list(
                    csv.DictReader(file, delimiter=",", quotechar='"')
                )
                if report_type == "simples":
                    return SimpleReport.generate(product_reader)
                elif report_type == "completo":
                    return CompleteReport.generate(product_reader)
                else:
                    raise ValueError
