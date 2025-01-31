from exercise import log_exercise, show_summery
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
            log_exercise()
        elif choice == 2:
            show_summery()
        elif choice == 3:
            print("Exiting the Fitness Tracker , Goodbye !")
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
