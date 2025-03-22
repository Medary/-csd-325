


def main():
    print("")  # Empty spacers to make the output look cleaner

    print("This program gets a persons first, middle, and last names and ")
    print("displays their first, middle, and last initials.")

    print("")  # Empty spacers to make the output look cleaner
    print("")  # Empty spacers to make the output look cleaner

    # This captures the users first name for the string
    first_string = input("Please enter your first name: ")

    print("")  # Empty spacers to make the output look cleaner

    # This captures the users middle name for the string
    middle_string = input("Please enter your middle name: ")

    print("")  # Empty spacers to make the output look cleaner

    # This captures the users last name for the string
    last_string = input("Please enter your last name: ")

    print("")  # Empty spacers to make the output look cleaner
    print("")  # Empty spacers to make the output look cleaner

    # This displays the users first, middle, and last initials
    print("Your initials are: " + first_string[0] + ". " + \
          middle_string[0] + ". " + last_string[0] + ".")


main()