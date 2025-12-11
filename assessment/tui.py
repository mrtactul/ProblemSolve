"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def display_welcome():
    """
    Display a welcome message when the program starts.
    This function shows the program title and provides initial user feedback.
    """
    print("=" * 60)
    print("  Disneyland Reviews Analysis System")
    print("=" * 60)
    print()


def display_main_menu():
    """
    Display the main menu options to the user.
    This shows the three main sections: View Data, Visualise Data, and Export Data.
    """
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
    Get the user's menu choice and return it.
    This function prompts the user to enter their selection.
    
    Returns:
        str: The user's menu choice (uppercase)
    """
    choice = input("\nPlease enter your choice: ").strip().upper()
    return choice


def display_view_data_menu():
    """
    Display the sub-menu for View Data options (Section A).
    This menu appears when the user selects 'A' from the main menu.
    """
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
    """
    Display the sub-menu for Visualise Data options (Section B).
    This menu appears when the user selects 'B' from the main menu.
    """
    print("\n" + "-" * 60)
    print("  VISUALISE DATA MENU")
    print("-" * 60)
    print("  [1] Pie chart - Reviews per park")
    print("  [2] Bar chart - Top 10 locations by rating")
    print("  [3] Bar chart - Average rating by month")
    print("  [X] Return to main menu")
    print("-" * 60)


def display_export_menu():
    """
    Display the sub-menu for Export Data options (Section D).
    This menu appears when the user selects 'C' from the main menu.
    """
    print("\n" + "-" * 60)
    print("  EXPORT DATA MENU")
    print("-" * 60)
    print("  [1] Export as TXT")
    print("  [2] Export as CSV")
    print("  [3] Export as JSON")
    print("  [X] Return to main menu")
    print("-" * 60)


def get_submenu_choice():
    """
    Get the user's sub-menu choice.
    
    Returns:
        str: The user's sub-menu choice (uppercase)
    """
    choice = input("\nPlease enter your choice: ").strip().upper()
    return choice


def display_message(message):
    """
    Display a general message to the user.
    
    Args:
        message (str): The message to display
    """
    print(message)


def get_user_input(prompt):
    """
    Get input from the user with a custom prompt.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        str: The user's input
    """
    return input(prompt).strip()


def display_error(message):
    """
    Display an error message to the user.
    
    Args:
        message (str): The error message to display
    """
    print(f"\n⚠ ERROR: {message}\n")


def display_reviews(reviews):
    """
    Display a list of reviews in a readable format.
    
    Args:
        reviews (list): List of review dictionaries to display
    """
    if not reviews:
        print("\nNo reviews found.")
        return

    print(f"\nFound {len(reviews)} reviews:")
    print("-" * 60)
    
    # Show first 5 reviews to avoid overwhelming the user
    # (The requirement asks to display all, but practically we might want to paginate)
    # For this assessment, we'll just show them all but with a separator
    
    for i, review in enumerate(reviews, 1):
        print(f"Review #{i}")
        print(f"Park: {review.get('Branch', 'N/A')}")
        print(f"Rating: {review.get('Rating', 'N/A')}/5")
        print(f"Location: {review.get('Reviewer_Location', 'N/A')}")
        print(f"Date: {review.get('Year_Month', 'N/A')}")
        print("-" * 30)

