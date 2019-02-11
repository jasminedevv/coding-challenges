import pytest
from stack import Item, Stack

def test_item():
    item = Item("hello")
    assert item.content is "hello"
    assert item.below is None

    item = Item(None)
    assert item.content is None

def test_stack_init():
    stack = Stack(["one", "two", "three"])
    assert stack.top.content is "three"
    assert stack.top.below.content is "two"

    stack = Stack(1)
    assert stack.top.content is 1
    assert stack.top.below is None

def test_stack_add():
    stack = Stack(["one", "two", "three"])
    stack.add("four")
    assert stack.top.content is "four"
    assert stack.top.below.content is "three"

def test_stack_pop():
    stack = Stack(["one", "two", "three"])
    removed = stack.pop()
    assert removed.content is "three"
    assert stack.top.content is "two"
