import dataclasses
import pytest
from main import Money


def test_is_a_dataclass_with_two_fields():
    assert dataclasses.is_dataclass(Money)
    assert [f.name for f in dataclasses.fields(Money)] == ["currency", "amount_cents"]


def test_fields_and_repr():
    m = Money("USD", 1050)
    assert m.currency == "USD"
    assert m.amount_cents == 1050
    assert repr(m) == "Money(currency='USD', amount_cents=1050)"


def test_equality_by_value():
    assert Money("USD", 100) == Money("USD", 100)
    assert Money("USD", 100) != Money("USD", 101)
    assert Money("USD", 100) != Money("EUR", 100)


def test_hash_agrees_with_equality():
    assert hash(Money("USD", 5)) == hash(Money("USD", 5))
    assert len({Money("USD", 5), Money("USD", 5), Money("EUR", 5)}) == 2


def test_usable_as_dict_key():
    prices = {Money("USD", 100): "a"}
    assert prices[Money("USD", 100)] == "a"


def test_immutable():
    m = Money("USD", 100)
    with pytest.raises(dataclasses.FrozenInstanceError):
        m.amount_cents = 5


def test_ordering_by_currency_then_amount():
    items = [Money("USD", 300), Money("EUR", 900), Money("USD", 100)]
    assert sorted(items) == [Money("EUR", 900), Money("USD", 100), Money("USD", 300)]
    assert Money("USD", 100) < Money("USD", 200)
    assert Money("USD", 200) >= Money("USD", 200)


def test_str_format():
    assert str(Money("USD", 1050)) == "10.50 USD"
    assert str(Money("USD", 5)) == "0.05 USD"
    assert str(Money("EUR", 0)) == "0.00 EUR"
    assert str(Money("USD", 100)) == "1.00 USD"


def test_add_same_currency():
    a, b = Money("USD", 100), Money("USD", 250)
    assert a + b == Money("USD", 350)
    assert a == Money("USD", 100)


def test_add_different_currency_raises():
    with pytest.raises(ValueError):
        Money("USD", 1) + Money("EUR", 1)


def test_add_non_money_raises_type_error():
    with pytest.raises(TypeError):
        Money("USD", 1) + 5


def test_validation_on_creation():
    with pytest.raises(TypeError):
        Money("USD", 10.5)
    with pytest.raises(ValueError):
        Money("", 100)
    with pytest.raises(ValueError):
        Money("USD", -1)