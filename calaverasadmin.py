from calaverasmodels import Item

def admin_add_item(character, item):
    if not isinstance(item, Item):
        raise ValueError("Invalid item")

    character.inventory.append(item)

def admin_remove_item(character, unique_id):
    character.inventory = [
        item for item in character.inventory
        if item.unique_id != unique_id
    ]

def admin_update_quantity(character, unique_id, quantity):
    for item in character.inventory:
        if item.unique_id == unique_id:
            item.quantity = quantity
            return
    raise ValueError("Item not found")