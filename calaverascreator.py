from calaverasdata import heritages, professions, profession_starting_items
from calaverasmodels import Character, Item
from calaverashelpers import get_non_empty_input, choose_from_list, normalize_name

def create_manual_character():
    name = normalize_name(get_non_empty_input("Enter character name: "))

    chosen_heritage = choose_from_list(
        heritages,
        "Choose a heritage:"
    )

    chosen_profession = choose_from_list(
        professions,
        "Choose a profession:"
    )

    inventory = [
    Item(name=item_name, quantity=1)
    for item_name in profession_starting_items[chosen_profession]
]

    return Character(
    name=name,
    heritage=chosen_heritage,
    profession=chosen_profession,
    inventory=inventory
)
