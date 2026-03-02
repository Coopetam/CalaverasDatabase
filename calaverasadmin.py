from calaverasmodels import Item
from calaverasdata import CURRENCY_NAME
from calaverasstorage import save_character


def admin_add_item(character, item):
    if not isinstance(item, Item):
        raise ValueError("Invalid item.")

    # Enforce single currency rule
    if item.name == CURRENCY_NAME:
        existing = character.get_currency()
        if existing:
            raise ValueError("Character already has currency.")

    if item.quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    character.inventory.append(item)
    save_character(character)


def admin_remove_item(character, unique_id):
    original_length = len(character.inventory)

    character.inventory = [
        item for item in character.inventory
        if item.unique_id != unique_id
    ]

    if len(character.inventory) == original_length:
        raise ValueError("Item not found.")

    save_character(character)


def admin_update_quantity(character, unique_id, quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    for item in character.inventory:
        if item.unique_id == unique_id:

            # Currency allows float
            if item.name == CURRENCY_NAME:
                item.quantity = float(quantity)

            # Standard items must be int
            else:
                if not isinstance(quantity, int):
                    raise ValueError(
                        "Standard item quantities must be integers."
                    )
                item.quantity = quantity

            save_character(character)
            return

    raise ValueError("Item not found.")
