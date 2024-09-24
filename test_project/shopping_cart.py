# WHAT WE WILL LEARN
# How to write and run a unit test using pytest
# How to use assert to validate code logic

# NAMING CONVENTIONS FOR A TEST FILE
# 1. test_anyname_that_you_like.py
# 2. anyname_that_you_like_test.py
# The directory is usually called "test"

class ShoppingCart:
    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size

    def add(self, item):
        if self.size() == self.max_size:
            raise OverflowError(f"Cannot add more than {self.max_size}")
        self.items.append(item)

    def remove(self):
        pass

    def size(self):
        return len(self.items)

    def get_items(self):
        return self.items

    def get_total_price(self):
        pass
