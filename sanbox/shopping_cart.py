def sum_items(cart):
    total = 0
    for stuff in cart.values():
        if stuff in shopping_list[0]:
            total += shopping_list[0][stuff]
    return total


def listed_cart(cart):
    for k, v in cart.items():
        print(f"'{k}: {v}'")


def listed_shopping(shopping_list):
    for thing in shopping_list:
        for k, v in thing.items():
            print(f"'{k}: {v}'")


print("Welcome Itoro's shopping mall")
shopping_list = [{"cookies": 599.20, "milk": 200.00, "eggs": 545.99,
                  "toys": 785.21, "chicken": 356.90, "yoghurt": 340.00,
                  "drinks": 555.00, "sugar": 977.88}]

while True:
    choice = int(input("Enter \n 0-to-exit; \n 1-to add item; \n 2-to remove item; \n 3-to view items in your cart \n"))
    
    if choice == 0:
        break

    if choice == 1:
        print("You can only add 5 items.")
        print("Here are the available items: ")
        listed_shopping(shopping_list)
        cart = {}
        for i in range(1, 6):
            item = input("Enter an item: ")
            if item in shopping_list[0]:
                cart.update({f"item{i}": f"{item}"})
                print(f"You have {i} item in the cart")
                for key, value in cart.items():
                    print(f"'{key}: {value}'")
            else:
                print("Sorry! We do not have this item")
            
        checkout = int(input("Press 0 to checkout cart; \n Press 1 to remove an item \n"))
        if checkout == 0:
            print("The total sum of all items in your cart is: ")
            print(sum_items(cart))
        elif checkout == 1:
            item2remove = input("Select an item you want to remove: ")
            if item2remove in cart.values():
                new_cart = {k: v for k, v in cart.items() if v != item2remove}
                print(f"{item2remove} has been removed successfully")
                print("Here are the items in your cart: ")
                listed_cart(new_cart)
            else:
                print("The selected item is not in the cart")

    elif choice == 2:
        print("Here are the items in your cart: ")
        listed_cart(cart)
        del_choice = input("Enter 0 to empty the cart or an item you want to remove: ")
        if del_choice in cart.values():
            new_cart = {k: v for k, v in cart.items() if v != del_choice}
            print(f"{del_choice} has been removed successfully")
            print("Here are the items in your cart: ")
            listed_cart(new_cart)
        elif int(del_choice) == 0:
            cart.clear()
            print("Your cart is empty.")
        else:
            print("You have entered a wrong input")
    elif choice == 3:
        print("Here are the items in your cart: ")
        listed_cart(cart)


"""
DRY - Don't Repeat Yourself

"""

