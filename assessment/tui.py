"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def _get_choice(prompt, valid_choices):
    """
    Internal helper: repeatedly ask for input until a valid choice is entered.

    Args:
        prompt (str): Prompt shown to user
        valid_choices (set[str]): Allowed choices (must already be uppercase strings)

    Returns:
        str: Validated choice (uppercase)
    """
    while True:
        choice = input(prompt).strip().upper()
        if choice in valid_choices:
            return choice
        display_error(f"Invalid choice '{choice}'. Please enter one of: {', '.join(sorted(valid_choices))}.")


def display_welcome():
    """Display a welcome message when the program starts."""
    print("=" * 60)
    print("  Disneyland Reviews Analysis System")
    print("=" * 60)
    print()


def display_main_menu():
    """Display the main menu options to the user."""
    print("\n" + "-" * 60)
    print("  MAIN MENU")
    print("-" * 60)
    print("  [A] View Data")
    print("  [B] Visualise Data")
    print("  [C] Export Data")
    print("  [X] Exit")
    print("-" * 60)


def get_menu_choice():
    """
    Get a validated main-menu choice.

    Returns:
        str: One of A, B, C, X
    """
    return _get_choice("\nPlease enter your choice: ", {"A", "B", "C", "X"})


def display_view_data_menu():
    """Display the sub-menu for View Data options (Section A)."""
    print("\n" + "-" * 60)
    print("  VIEW DATA MENU")
    print("-" * 60)
    print("  [1] Display all reviews for a specific park")
    print("  [2] Count reviews by park and location")
    print("  [3] Average rating by park and year")
    print("  [4] Average score per park by reviewer location")
    print("  [X] Return to main menu")
    print("-" * 60)


def display_visualise_menu():
    """Display the sub-menu for Visualise Data options (Section B)."""
    print("\n" + "-" * 60)
    print("  VISUALISE DATA MENU")
    print("-" * 60)
    print("  [1] Pie chart - Reviews per park")
    print("  [2] Bar chart - Top 10 locations by rating")
    print("  [3] Bar chart - Average rating by month")
    print("  [X] Return to main menu")
    print("-" * 60)


def display_export_menu():
    """Display the sub-menu for Export Data options (Section D)."""
    print("\n" + "-" * 60)
    print("  EXPORT DATA MENU")
    print("-" * 60)
    print("  [1] Export as TXT")
    print("  [2] Export as CSV")
    print("  [3] Export as JSON")
    print("  [X] Return to main menu")
    print("-" * 60)


def get_view_data_choice():
    """Get a validated choice for the View Data menu."""
    return _get_choice("\nPlease enter your choice: ", {"1", "2", "3", "4", "X"})


def get_visualise_choice():
    """Get a validated choice for the Visualise Data menu."""
    return _get_choice("\nPlease enter your choice: ", {"1", "2", "3", "X"})


def get_export_choice():
    """Get a validated choice for the Export Data menu."""
    return _get_choice("\nPlease enter your choice: ", {"1", "2", "3", "X"})


def display_message(message):
    """Display a general message to the user."""
    print(message)


def get_user_input(prompt):
    """Get input from the user with a custom prompt."""
    return input(prompt).strip()


def pause():
    """Pause so the user can read output before returning to menus."""
    input("\nPress Enter to continue...")


def display_error(message):
    """Display an error message to the user."""
    print(f"\n⚠ ERROR: {message}\n")


def display_reviews(reviews, limit=None):
    """
    Display a list of reviews in a readable format.

    Args:
        reviews (list): List of review dictionaries to display
        limit (int|None): Optional max number of reviews to display.
                          None means display all (matches assessment requirement).
    """
    if not reviews:
        print("\nNo reviews found.")
        return

    total = len(reviews)
    print(f"\nFound {total} reviews:")
    print("-" * 60)

    to_show = reviews if limit is None else reviews[:limit]

    for i, review in enumerate(to_show, 1):
        print(f"Review #{i}")
        print(f"Park: {review.get('Branch', 'N/A')}")
        print(f"Rating: {review.get('Rating', 'N/A')}/5")
        print(f"Location: {review.get('Reviewer_Location', 'N/A')}")
        print(f"Date: {review.get('Year_Month', 'N/A')}")
        print("-" * 30)

    if limit is not None and total > limit:
        print(f"... showing {limit} of {total} reviews.")
