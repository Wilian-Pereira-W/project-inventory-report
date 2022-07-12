from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def get_stocked_products(self, list):
        results = "Produtos estocados por empresa:\n"
        for chave, value in Counter(list).items():
            results += f"- {chave}: {value}\n"
        return results

    @classmethod
    def generate(self, list_product):
        companies = []
        results = SimpleReport.generate(list_product)
        for product in list_product:
            companies.append(product["nome_da_empresa"])

        stocked_products = self.get_stocked_products(companies)
        return f"{results}\n" f"{stocked_products}"
