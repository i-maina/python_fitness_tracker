from input_validation import get_positive_integer


def ask_for_choice():
    print("Welcome to the Fitness Tracker !")
    print("1. Log exercise")
    print("2. Show summery")
    print("3. Exit")
    choice = get_positive_integer()
    return choice


def main():
    while True:
        choice = ask_for_choice()
        if choice == 1:
            pass
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
