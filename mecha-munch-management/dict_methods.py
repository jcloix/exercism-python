"""Functions to manage a users shopping cart items."""


from collections import Counter


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    

    for item in items_to_add:
        current_cart.setdefault(item, 0)
        current_cart[item] += 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    return dict(Counter(notes))


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    ideas.update(recipe_updates)
    return ideas
    



def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))



def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """

    fulfillment = {}
    for item, quantity in sorted(cart.items(), reverse=True):  # reverse alpha
        aisle_info = aisle_mapping.get(item, {})
        fulfillment[item] = [quantity, *aisle_info]
    return fulfillment


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory.
    :return: dict - updated store_inventory.
    """
    for item, (qty, *_rest) in fulfillment_cart.items():
        inventory = store_inventory.get(item)
        if not inventory or not isinstance(inventory[0], int):
            continue

        stock = inventory[0] - qty
        inventory[0] = stock if stock > 0 else "Out of Stock"

    return store_inventory
