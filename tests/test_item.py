"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 3)
item2 = Item("Ноутбук", 20000, 1)


def test_calculate_total_price():

    assert item1.calculate_total_price() == 30000
    assert item2.calculate_total_price() == 20000


def test_apply_discount():

    Item.pay_rate = 0.5

    item1.apply_discount()
    item2.apply_discount()

    assert item1.price == 5000.0
    assert item2.price == 10000.0

def test_item_attributes():

    assert item1.name == "Смартфон"
    assert item2.name == "Ноутбук"
    assert item1.price == 5000
    assert item2.price == 10000
    assert item1.quantity == 3
    assert item2.quantity == 1

    assert len(Item.all) == 2

    item3 = Item("Монитор", 5000, 10)

    assert len(Item.all) == 3
