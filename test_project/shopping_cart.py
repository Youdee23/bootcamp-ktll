# WHAT WE WILL LEARN
# How to write and run a unit test using pytest
# How to use assert to validate code logic

# NAMING CONVENTIONS FOR A TEST FILE
# 1. test_anyname_that_you_like.py
# 2. anyname_that_you_like_test.py
# The directory is usually called "test"

# FIXTURES
# Fixtures are used to initialize test functions. They
# provide a fixed baseline so that tests execute reliably
# and produce consistent , repeatedable results. They are
# accessed by test functions as arguement.

# A fixture is typically a normal Python function.
# To create a fixture, we use a decorator @pytest.fixture
# annotation. Then we use that function as an arguement in
# our test.

# MOCKING DEPENDENCIES - Read this up

class ShoppingCart:
    def __init__(self, max_size: int = 5) -> None:
        self.items = []
        self.max_size = max_size
        self.price = []

    def add(self, item: str) -> None:
        if self.size() == self.max_size:
            raise OverflowError(f"Cannot add more than {self.max_size}")
        self.items.append(item)

    def remove(self):
        pass

    def size(self):
        return len(self.items)

    def get_items(self):
        return self.items

    def get_total_price(self, price_map: dict[str, int]) -> int:
        total_price: int = 0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price
