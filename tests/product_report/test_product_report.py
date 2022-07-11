from inventory_report.inventory.product import Product
import pytest


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


def test_relatorio_produto(product):
    print(repr(product))
    assert (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    ) in repr(product)
    assert (
        "O produto Xbox Series x"
        " fabricado em 2021-07-18"
        " por Microsoft com validade"
        " até 2035-10-05"
        " precisa ser armazenado Qualquer lugar."
    ) in repr(product)
    assert ("validade") in repr(product)
