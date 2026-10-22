import pytest
from todo import TodoList

def test_add_task():
    tl = TodoList()
    assert tl.add_task("Купить молоко") == 1
    assert len(tl.get_tasks()) == 1

def test_add_empty_task():
    tl = TodoList()
    with pytest.raises(ValueError):
        tl.add_task("")

def test_mark_done():
    tl = TodoList()
    tl.add_task("Сделать ДЗ")
    tl.mark_done(0)
    assert tl.count_done() == 1

def test_mark_done_invalid_index():
    tl = TodoList()
    with pytest.raises(IndexError):
        tl.mark_done(5)
def test_delete_task():
    tl = TodoList()
    tl.add_task("Задача 1")
    tl.add_task("Задача 2")
    removed = tl.delete_task(0)
    assert removed["title"] == "Задача 1"
    assert len(tl.get_tasks()) == 1

def test_delete_invalid_index():
    tl = TodoList()
    with pytest.raises(IndexError):
        tl.delete_task(10)