from calaverascreator import create_manual_character


def main():
    print("=== Calaveras Character Creation ===\n")

    character = create_manual_character()

    print("\nCharacter Created Successfully!")
    print(f"Name: {character.name}")
    print(f"Heritage: {character.heritage}")
    print(f"Profession: {character.profession}")


if __name__ == "__main__":
    main()
