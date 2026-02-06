import uuid  # standard Python library





class Character:
    def __init__(
        self,
        name,
        heritage,
        profession,
        inventory=None,
        deaths=0,
        curses=None,
        afflictions=None,
        notes=""
    ):
        self.name = name
        self.heritage = heritage
        self.profession = profession

        self.inventory = inventory or []
        self.deaths = deaths
        self.curses = curses if curses is not None else []
        self.afflictions = afflictions if afflictions is not None else []

        self.notes = notes

    def to_dict(self):
        return {
            "name": self.name,
            "heritage": self.heritage,
            "profession": self.profession,
            "deaths": self.deaths,
            "curses": self.curses,
            "afflictions": self.afflictions,
            "inventory": [item.to_dict() for item in self.inventory],
            "notes": self.notes
        }

    # --- Admin Status Methods ---

    def add_curse(self, curse_name):
        if curse_name not in self.curses:
            self.curses.append(curse_name)

    def remove_curse(self, curse_name):
        if curse_name in self.curses:
            self.curses.remove(curse_name)

    def add_affliction(self, affliction_name):
        if affliction_name not in self.afflictions:
            self.afflictions.append(affliction_name)

    def remove_affliction(self, affliction_name):
        if affliction_name in self.afflictions:
            self.afflictions.remove(affliction_name)

    def increment_death(self):
        self.deaths += 1

    @staticmethod
    def from_dict(data):
        inventory = [
            Item.from_dict(item_data)
            for item_data in data.get("inventory", [])
        ]

        return Character(
            name=data["name"],
            heritage=data["heritage"],
            profession=data["profession"],
            inventory=inventory,
            deaths=data.get("deaths", 0),
            curses=data.get("curses", []),
            afflictions=data.get("afflictions", []),
            notes=data.get("notes", "")
        )


class Item:
    def __init__(self, name, quantity, is_custom=False, unique_id=None):
        self.name = name
        self.quantity = quantity
        self.is_custom = is_custom
        self.unique_id = unique_id or (str(uuid.uuid4()) if is_custom else None)

    def to_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "is_custom": self.is_custom,
            "unique_id": self.unique_id

        }


    @staticmethod
    def from_dict(data):
        return Item(
            name=data["name"],
            quantity=data["quantity"],
            is_custom=data.get("is_custom", False),
            unique_id=data.get("unique_id")
    )

