from calaverasdata import heritages, professions
from calaverasmodels import Character
from calaverashelpers import get_non_empty_input, choose_from_list

def create_manual_character():
    name = get_non_empty_input("Enter character name: ")

    chosen_heritage = choose_from_list(
        heritages,
        "Choose a heritage:"
    )

    chosen_profession = choose_from_list(
        professions,
        "Choose a profession:"
    )

    return Character(
        name=name,
        heritage=chosen_heritage,
        profession=chosen_profession
    )