import pytest as pytest

@pytest.mark.parametrize("test_input, expected", [(6, 0), (7, 1), (8, 2)])
def test_first_request(test_input, expected):
    assert (test_input % 3) == expected

def test_second_request():
    assert 3 == int("3")

@pytest.mark.parametrize("test_input, expected", [(0, -5), (15, 10), pytest.param(1000, 0, marks=pytest.mark.xfail)])
def test_third_request(test_input, expected):
    assert (test_input - 5) == expected

def test_fourth_request():
    d = {"water_boiling_temperature": 100, "water_freezing_temperature": 0}
    assert d["water_freezing_temperature"] < d["water_boiling_temperature"]

def test_fifth_request():
    d = {"a": 1, "b": 3, "c": 10}
    e = {"a": 20, "b": 60, "c": 200}
    assert d["a"] * 20 == e["a"]
    assert d["b"] * 20 == e["b"]
    assert d["c"] * 20 == e["c"]

from collections import namedtuple
Task = namedtuple('Task', ['name', 'city', 'phone', 'email'])
Task.__new__.__defaults__ = (None, None, None, None)
def test_six_request():
    t = Task('Моисей', 'Москва')
    assert t.name == 'Моисей'
    assert t.city == 'Москва'
    assert (t.phone, t.email) == (None, None)