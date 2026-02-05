"""
This module is responsible for processing the data. It will largely contain functions that will receive the overall dataset and
perform necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import csv


def _norm(text):
    """Normalise text for case-insensitive matching."""
    return str(text).strip().lower()


def load_data(filepath):
    """
    Load data from a CSV file and return it as a list of dictionaries.
    Each row in the CSV becomes a dictionary with column names as keys.

    Args:
        filepath (str): The path to the CSV file to load

    Returns:
        list: A list of dictionaries, where each dictionary represents a row from the CSV.
    """
    data = []
    try:
        with open(filepath, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        # Processing module should not print UI messages.
        return []
    except Exception:
        return []

    return data


def filter_reviews_by_park(data, park_name):
    """
    Filter reviews to get only those for a specific park (Task 7).

    Args:
        data (list): The list of all reviews
        park_name (str): The name of the park to filter by

    Returns:
        list: A list of reviews (dictionaries) for the specified park
    """
    target = _norm(park_name)
    if not target:
        return []

    filtered = []
    for review in data:
        branch = _norm(review.get("Branch", ""))
        if target in branch:
            filtered.append(review)

    return filtered


def count_reviews_by_park_and_location(data, park_name, location):
    """
    Count how many reviews a park received from a specific location (Task 8).

    Args:
        data (list): The list of all reviews
        park_name (str): The name of the park
        location (str): The reviewer's location

    Returns:
        int: The number of matching reviews
    """
    target_park = _norm(park_name)
    target_location = _norm(location)

    if not target_park or not target_location:
        return 0

    count = 0
    for review in data:
        branch = _norm(review.get("Branch", ""))
        reviewer_location = _norm(review.get("Reviewer_Location", ""))

        if target_park in branch and target_location in reviewer_location:
            count += 1

    return count


def calculate_average_rating_by_year(data, park_name, year):
    """
    Calculate the average rating for a park in a specific year (Task 9).

    Args:
        data (list): The list of all reviews
        park_name (str): The name of the park
        year (str|int): The year to filter by (YYYY)

    Returns:
        float|None: The average rating, or None if no reviews found
    """
    target_park = _norm(park_name)
    target_year = str(year).strip()

    if not target_park or len(target_year) != 4 or not target_year.isdigit():
        return None

    total_rating = 0
    count = 0

    for review in data:
        branch = _norm(review.get("Branch", ""))
        review_date = str(review.get("Year_Month", "")).strip()

        if target_park in branch and review_date.startswith(target_year):
            try:
                rating = int(review.get("Rating", 0))
            except ValueError:
                continue

            total_rating += rating
            count += 1

    if count == 0:
        return None

    return total_rating / count


def count_reviews_per_park(data):
    """
    Count the number of reviews for each park (Task 10).

    Args:
        data (list): The list of all reviews

    Returns:
        dict: Keys are park names, values are review counts
    """
    counts = {}
    for review in data:
        branch = review.get("Branch", "Unknown")
        counts[branch] = counts.get(branch, 0) + 1
    return counts


def get_top_locations_by_rating(data, park_name, top_n=10):
    """
    Find locations with the highest average rating for a specific park (Task 11).

    Args:
        data (list): The list of all reviews
        park_name (str): The park to analyse
        top_n (int): Number of top locations to return

    Returns:
        tuple: (list of locations, list of average ratings)
    """
    target_park = _norm(park_name)
    if not target_park:
        return [], []

    location_ratings = {}  # {location: [sum_ratings, count]}

    for review in data:
        branch = _norm(review.get("Branch", ""))
        if target_park not in branch:
            continue

        location = review.get("Reviewer_Location", "Unknown")
        try:
            rating = int(review.get("Rating", 0))
        except ValueError:
            continue

        if location not in location_ratings:
            location_ratings[location] = [0, 0]

        location_ratings[location][0] += rating
        location_ratings[location][1] += 1

    averages = []
    for location, stats in location_ratings.items():
        if stats[1] > 0:
            averages.append((location, stats[0] / stats[1]))

    averages.sort(key=lambda x: x[1], reverse=True)
    top_results = averages[:top_n]

    locations = [item[0] for item in top_results]
    ratings = [item[1] for item in top_results]
    return locations, ratings


def calculate_monthly_averages(data, park_name):
    """
    Calculate average rating for each month for a specific park (Task 12).

    Args:
        data (list): The list of all reviews
        park_name (str): The park to analyse

    Returns:
        tuple: (list of month names, list of average ratings)
    """
    target_park = _norm(park_name)
    if not target_park:
        return [], []

    month_stats = {i: {"sum": 0, "count": 0} for i in range(1, 13)}

    for review in data:
        branch = _norm(review.get("Branch", ""))
        if target_park not in branch:
            continue

        year_month = str(review.get("Year_Month", "")).strip()
        if "-" not in year_month:
            continue

        parts = year_month.split("-")
        if len(parts) != 2:
            continue

        try:
            month = int(parts[1])
            rating = int(review.get("Rating", 0))
        except ValueError:
            continue

        if 1 <= month <= 12:
            month_stats[month]["sum"] += rating
            month_stats[month]["count"] += 1

    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                   "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    ratings = []
    for i in range(1, 13):
        stats = month_stats[i]
        ratings.append(stats["sum"] / stats["count"] if stats["count"] else 0)

    return month_names, ratings


def calculate_park_location_averages(data):
    """
    Calculate the average rating for every park from every location (Task 13).

    Args:
        data (list): The list of all reviews

    Returns:
        dict: Nested dictionary {park: {location: average_rating}}
    """
    stats = {}  # {park: {location: {'sum': 0, 'count': 0}}}

    for review in data:
        branch = review.get("Branch", "Unknown")
        location = review.get("Reviewer_Location", "Unknown")

        try:
            rating = int(review.get("Rating", 0))
        except ValueError:
            continue

        if branch not in stats:
            stats[branch] = {}

        if location not in stats[branch]:
            stats[branch][location] = {"sum": 0, "count": 0}

        stats[branch][location]["sum"] += rating
        stats[branch][location]["count"] += 1

    results = {}
    for park, locations in stats.items():
        results[park] = {}
        for loc, values in locations.items():
            if values["count"]:
                results[park][loc] = values["sum"] / values["count"]

    return results
