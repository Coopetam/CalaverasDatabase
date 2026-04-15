from calaverasdata import heritages, professions, profession_starting_items
from calaverasmodels import Character, Item
from calaverashelpers import get_non_empty_input, choose_from_list, normalize_name
from calaverasapp import db


def create_manual_character():
    name = normalize_name(get_non_empty_input("Enter character name: "))

    chosen_heritage = choose_from_list(heritages, "Choose a heritage:")
    chosen_profession = choose_from_list(professions, "Choose a profession:")

    new_character = Character(
        name=name,
        heritage=chosen_heritage,   # TEMP mapping
        profession=chosen_profession   # TEMP mapping
    )

    db.session.add(new_character)
    db.session.commit()

    return new_character