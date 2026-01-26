def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.\n")


def choose_from_list(options, prompt):
    while True:
        print(prompt)
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        choice = input("Enter number: ").strip()

        if not choice.isdigit():
            print("Please enter a number.\n")
            continue

        index = int(choice) - 1

        if 0 <= index < len(options):
            return options[index]

        print("That number is not an option.\n")


def normalize_name(name):
    return name.strip().title()
