"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt


def plot_reviews_pie_chart(counts):
    """
    Create a pie chart showing the number of reviews per park.

    Args:
        counts (dict): Dictionary with park names as keys and counts as values
    """
    if not counts:
        return

    labels = list(counts.keys())
    values = list(counts.values())

    plt.figure(figsize=(10, 8))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.axis("equal")
    plt.title("Distribution of Reviews per Park")

    plt.tight_layout()
    plt.show()
    plt.close()


def plot_top_locations_bar_chart(locations, ratings, park_name):
    """
    Create a bar chart of the top locations by average rating.

    Args:
        locations (list): List of location names
        ratings (list): List of average ratings
        park_name (str): Name of the park being analysed
    """
    if not locations or not ratings:
        return

    plt.figure(figsize=(12, 6))
    plt.bar(locations, ratings)

    plt.xlabel("Reviewer Location")
    plt.ylabel("Average Rating")
    plt.title(f"Top {len(locations)} Locations by Average Rating for {park_name}")

    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 5.5)
    plt.grid(axis="y")

    plt.tight_layout()
    plt.show()
    plt.close()


def plot_monthly_ratings_bar_chart(months, ratings, park_name):
    """
    Create a bar chart of average ratings by month.

    Args:
        months (list): List of month names
        ratings (list): List of average ratings
        park_name (str): Name of the park being analysed
    """
    if not months or not ratings:
        return

    plt.figure(figsize=(12, 6))
    plt.bar(months, ratings)

    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.title(f"Average Monthly Rating for {park_name}")

    plt.ylim(0, 5.5)
    plt.grid(axis="y")

    plt.tight_layout()
    plt.show()
    plt.close()
