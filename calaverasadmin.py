from calaverasmodels import Item
from calaverasdata import CURRENCY_NAME
from calaverasapp import db


def admin_add_item(character, item):
    if not isinstance(item, Item):
        raise ValueError("Invalid item.")

    if item.name == CURRENCY_NAME:
        existing = character.get_currency()
        if existing:
            raise ValueError("Character already has currency.")

    if item.quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    character.inventory.append(item)
    db.session.commit()


def admin_remove_item(character, unique_id):
    original_length = len(character.inventory)

    character.inventory = [
        item for item in character.inventory
        if item.unique_id != unique_id
    ]

    if len(character.inventory) == original_length:
        raise ValueError("Item not found.")

    db.session.commit()


def admin_update_quantity(character, unique_id, quantity):
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    for item in character.inventory:
        if item.unique_id == unique_id:

            if item.name == CURRENCY_NAME:
                item.quantity = float(quantity)
            else:
                if not isinstance(quantity, int):
                    raise ValueError(
                        "Standard item quantities must be integers."
                    )
                item.quantity = quantity

            db.session.commit()
            return

    raise ValueError("Item not found.")