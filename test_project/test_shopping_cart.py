import pytest
from shopping_cart import ShoppingCart

@pytest.fixture
def cart():
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add("wig")
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item(cart):
    cart.add("wig")
    assert "wig" in cart.get_items()

def test_when_add_more_then_max_size(cart):
    with pytest.raises(OverflowError): # creates a context
        for _ in range(5): # 1,2,3,4,5,6
            cart.add("apple4")
        cart.add("apple")

def test_can_get_total_price(cart):
    cart.add("milk")
    cart.add("coffee")

    price_map = {
        "milk": 3000,
        "coffee": 900
    }

    assert cart.get_total_price(price_map) == 3900
