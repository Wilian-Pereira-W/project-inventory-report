import pytest
from inventory_report.inventory.product import Product


@pytest.fixture
def product():
    return Product(
        1,
        "Xbox Series x",
        "Microsoft",
        "2021-07-18",
        "2035-10-05",
        "123456789we",
        "Qualquer lugar",
    )


def test_cria_produto(product):
    assert product.id == 1
    assert product.nome_do_produto == "Xbox Series x"
    assert product.nome_da_empresa == "Microsoft"
    assert product.data_de_fabricacao == "2021-07-18"
    assert product.numero_de_serie == "123456789we"
    assert product.instrucoes_de_armazenamento == "Qualquer lugar"
    assert product.data_de_validade == "2035-10-05"
