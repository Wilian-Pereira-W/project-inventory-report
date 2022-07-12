from datetime import datetime


class SimpleReport:
    @classmethod
    def get_due_date(self, list):
        date = datetime.now()
        due_date = []
        for product in list:
            if product["data_de_validade"] > date.strftime("%Y-%m-%d"):
                due_date.append(product["data_de_validade"])
        return min(due_date)

    @classmethod
    def get_company_name(self, list):
        company_name = []
        repetidos = []
        for product in list:
            if product["nome_da_empresa"] not in company_name:
                company_name.append(product["nome_da_empresa"])
            else:
                repetidos.append(product["nome_da_empresa"])
        return repetidos[0]

    @classmethod
    def get_oldest_manuf_date(self, list):
        date = datetime.now()
        oldest_manuf_date = []
        for product in list:
            if product["data_de_fabricacao"] < date.strftime("%Y-%m-%d"):
                oldest_manuf_date.append(product["data_de_fabricacao"])

        return min(oldest_manuf_date)

    @classmethod
    def generate(self, list_product):
        due_date = self.get_due_date(list_product)
        oldest_manuf_date = self.get_oldest_manuf_date(list_product)
        company_name = self.get_company_name(list_product)

        return (
            f"Data de fabricação mais antiga: {oldest_manuf_date}\n"
            f"Data de validade mais próxima: {due_date}\n"
            f"Empresa com mais produtos: {company_name}"
        )
