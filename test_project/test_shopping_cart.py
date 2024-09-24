import pytest
from shopping_cart import ShoppingCart

def test_can_add_item_to_cart():
    cart = ShoppingCart(5)
    cart.add("wig")
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item():
    cart = ShoppingCart(5)
    cart.add("wig")
    assert "wig" in cart.get_items()

def test_when_add_more_then_max_size():
    cart = ShoppingCart(5)
    with pytest.raises(OverflowError): # creates a context
        for _ in range(5): # 1,2,3,4,5,6
            cart.add("apple4")
        cart.add("apple")

def test_can_get_total_price():
    pass
