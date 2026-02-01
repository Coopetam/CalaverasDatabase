import json
from calaverasmodels import Character


FILE_PATH = "characters.json"

def load_characters():
    """Load all character from storage"""
    try:
        with open (FILE_PATH, "r") as file:
            data = json.load(file)
            return [Character.from_dict(entry) for entry in data]
    except FileNotFoundError:
        return []
    
def save_character(character):
    """Save a single character to storage"""
    characters = load_characters()
    characters.append(character)

    with open(FILE_PATH, "w") as file:
        json.dump(
            [char.to_dict() for char in characters],
            file,
            indent=2
        )