"""
SectionA This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
from pathlib import Path

import tui
import process
import visual
import exporter


def main():
    """
    Main function that controls the program flow.
    This function:
    1. Displays welcome message
    2. Loads the data from CSV file
    3. Runs a continuous loop showing menus and handling user choices
    4. Exits when user chooses to exit
    """
    # Task 1: Display welcome message
    tui.display_welcome()

    # Task 2: Load data from CSV file (robust path handling)
    base_dir = Path(__file__).resolve().parent
    filepath = base_dir / "data" / "Disneyland_reviews.csv"

    # Fallback (in case your file is lowercase on your machine/repo)
    if not filepath.exists():
        filepath = base_dir / "data" / "disneyland_reviews.csv"

    data = process.load_data(str(filepath))

    # Display confirmation message with row count
    if data:
        row_count = len(data)
        tui.display_message("✓ Data loaded successfully!")
        tui.display_message(f"✓ Total number of reviews: {row_count:,}")
    else:
        tui.display_error(
            "Failed to load data. Please check the file path: "
            f"{filepath}"
        )
        return

    # Task 5: Continuous program loop
    running = True
    while running:
        # Task 3: Display main menu
        tui.display_main_menu()

        # Get user's menu choice
        choice = tui.get_menu_choice()

        # Task 4: Validate user input and confirm choice
        if choice == "A":
            tui.display_message("You selected: [A] View Data")
            handle_view_data_menu(data)
        elif choice == "B":
            tui.display_message("You selected: [B] Visualise Data")
            handle_visualise_menu(data)
        elif choice == "C":
            tui.display_message("You selected: [C] Export Data")
            handle_export_menu(data)
        elif choice == "X":
            tui.display_message("Thank you for using the Disneyland Reviews Analysis System!")
            tui.display_message("Goodbye!")
            running = False
        else:
            tui.display_error(f"Invalid choice '{choice}'. Please enter A, B, C, or X.")


def handle_view_data_menu(data):
    """
    Handle the View Data sub-menu (Task 6).
    Displays the sub-menu and processes user choices for Section A features.

    Args:
        data (list): The loaded dataset
    """
    while True:
        tui.display_view_data_menu()
        sub_choice = tui.get_submenu_choice()

        if sub_choice == "1":
            # Task 7: Display all reviews for a specific park
            park = tui.get_user_input("Enter park name: ")
            reviews = process.filter_reviews_by_park(data, park)
            tui.display_reviews(reviews)

        elif sub_choice == "2":
            # Task 8: Count reviews by park and location
            park = tui.get_user_input("Enter park name: ")
            location = tui.get_user_input("Enter reviewer location: ")
            count = process.count_reviews_by_park_and_location(data, park, location)
            tui.display_message(f"\nNumber of reviews for {park} from {location}: {count}")

        elif sub_choice == "3":
            # Task 9: Average rating by park and year
            park = tui.get_user_input("Enter park name: ")
            year = tui.get_user_input("Enter year (YYYY): ")
            average = process.calculate_average_rating_by_year(data, park, year)

            if average is not None:
                tui.display_message(f"\nAverage rating for {park} in {year}: {average:.2f}/5")
            else:
                tui.display_message(f"\nNo reviews found for {park} in {year}.")

        elif sub_choice == "4":
            # Task 13: Average score per park by reviewer location
            tui.display_message("Calculating average scores per park by location...")
            results = process.calculate_park_location_averages(data)

            for park, locations in results.items():
                tui.display_message(f"\nPARK: {park}")
                tui.display_message("-" * 30)

                for location, avg in sorted(locations.items())[:5]:
                    tui.display_message(f"{location}: {avg:.2f}/5")

                if len(locations) > 5:
                    tui.display_message(f"... and {len(locations) - 5} more locations.")

        elif sub_choice == "X":
            break
        else:
            tui.display_error(f"Invalid choice '{sub_choice}'. Please enter 1-4 or X.")


def handle_visualise_menu(data):
    """
    Handle the Visualise Data sub-menu (Task 6).
    Displays the sub-menu and processes user choices for visual features.

    Args:
        data (list): The loaded dataset
    """
    while True:
        tui.display_visualise_menu()
        sub_choice = tui.get_submenu_choice()

        if sub_choice == "1":
            # Task 10: Pie chart - Reviews per park
            counts = process.count_reviews_per_park(data)
            tui.display_message("Generating pie chart...")
            visual.plot_reviews_pie_chart(counts)

        elif sub_choice == "2":
            # Task 11: Bar chart - Top 10 locations by rating
            park = tui.get_user_input("Enter park name: ")
            locations, ratings = process.get_top_locations_by_rating(data, park)

            if locations:
                tui.display_message("Generating bar chart...")
                visual.plot_top_locations_bar_chart(locations, ratings, park)
            else:
                tui.display_message(f"No data found for park: {park}")

        elif sub_choice == "3":
            # Task 12: Bar chart - Average rating by month
            park = tui.get_user_input("Enter park name: ")
            months, ratings = process.calculate_monthly_averages(data, park)

            if sum(ratings) > 0:
                tui.display_message("Generating bar chart...")
                visual.plot_monthly_ratings_bar_chart(months, ratings, park)
            else:
                tui.display_message(f"No data found for park: {park}")

        elif sub_choice == "X":
            break
        else:
            tui.display_error(f"Invalid choice '{sub_choice}'. Please enter 1-3 or X.")


def handle_export_menu(data):
    """
    Handle the Export Data sub-menu (Task 14).

    Args:
        data (list): The loaded dataset
    """
    base_exporter = exporter.DataExporter()
    aggregate_data = base_exporter.prepare_aggregate_data(data)

    while True:
        tui.display_export_menu()
        sub_choice = tui.get_submenu_choice()

        filename = "park_reviews_summary"

        if sub_choice == "1":
            txt_exporter = exporter.TXTExporter()
            success, message = txt_exporter.export(aggregate_data, filename)
            tui.display_message(f"✓ {message}") if success else tui.display_error(message)

        elif sub_choice == "2":
            csv_exporter = exporter.CSVExporter()
            success, message = csv_exporter.export(aggregate_data, filename)
            tui.display_message(f"✓ {message}") if success else tui.display_error(message)

        elif sub_choice == "3":
            json_exporter = exporter.JSONExporter()
            success, message = json_exporter.export(aggregate_data, filename)
            tui.display_message(f"✓ {message}") if success else tui.display_error(message)

        elif sub_choice == "X":
            break
        else:
            tui.display_error(f"Invalid choice '{sub_choice}'. Please enter 1-3 or X.")


if __name__ == "__main__":
    main()
