from calaverascreator import create_manual_character
from calaverasstorage import save_character, load_characters

def main():
    print("=== Calaveras Character Creation ===\n")

    character = create_manual_character()
    save_character(character)

    print("\nCharacter Created Successfully!")
    print(f"Name: {character.name}")
    print(f"Heritage: {character.heritage}")
    print(f"Profession: {character.profession}")

    list_characters()


def list_characters():
    characters = load_characters()

    if not characters:
        print("No characters have been created yet.")
        return

    print("\n=== Character Roster ===")
    for index, character in enumerate(characters, start=1):
        print(f"{index}. {character.name}")


if __name__ == "__main__":
    main()
